#!/usr/bin/env python3
"""Atualiza data/precos_stock.csv a partir de uma exportação de stock do Odoo.

Aceita .xlsx ou .csv/.tsv com as colunas da exportação "Stocks" do Odoo:
  Produto | Categoria de Artigo | Unidade de medida | Quantidade Em Mão | A Chegar | Custo | Preço de Vendas | Margem

Guarda vinhos (categoria Vini) e destilados (Liquori e distillati). Só guarda SKU, nome, categoria,
formato, stock, a chegar e preço de venda trade. Custo e margem NUNCA são copiados.

Antes de gravar faz uma cópia de segurança (data/precos_stock.bak.csv). Não grava nada se a
exportação não tiver nenhum artigo da categoria Vini.

No fim lista:
  - artigos de vinho da exportação sem ficha no catálogo (novos, a pesquisar);
  - vinhos do catálogo sem nenhum SKU na exportação (possivelmente descontinuados).

Uso:
  python3 scripts/atualizar_precos.py exportacao_odoo.xlsx [--data 2026-10-01] [--sem-destilados]
"""
import argparse
import csv
import datetime
import json
import os
import re
import shutil
import sys
import zipfile
import xml.etree.ElementTree as ET

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOGO = os.path.join(BASE, "data", "catalogo.json")
PRECOS = os.path.join(BASE, "data", "precos_stock.csv")
BACKUP = os.path.join(BASE, "data", "precos_stock.bak.csv")
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
CATEGORIAS_VINHO = {"vini"}
CATEGORIAS_DESTILADOS = {"liquori e distillati"}
CAMPOS = ["sku", "nome_odoo", "categoria", "formato", "stock", "a_chegar", "preco_trade_eur",
          "preco_trade_eur_2024h2", "data"]

# ordem importa: packs e formatos compostos primeiro, 1,5 L antes de 5 L
FORMATOS = (
    (r"pack\s*of\s*3|3\s*x\s*0[,.]75", "3 x 0,75 L"),
    (r"6\s*garr|6\s*x\s*0[,.]75|cassa di legno da 6", "6 x 0,75 L"),
    (r"4\s*x\s*250\s*ml", "4 x 0,25 L"),
    (r"3\s*x\s*20\s*cl", "3 x 0,20 L"),
    (r"1[,.]5\s*L|magnum", "1,5 L"),
    (r"\b18\s*L\b", "18 L"),
    (r"\b12\s*L\b", "12 L"),
    (r"(?<![,.\d])6\s*L\b", "6 L"),
    (r"(?<![,.\d])5\s*L\b", "5 L"),
    (r"(?<![,.\d])3\s*L\b|jeroboam", "3 L"),
    (r"0[,.]375|375\s*ml|37[,.]5\s*cl", "0,375 L"),
    (r"0[,.]50?\s*L\b|50\s*cl\b", "0,50 L"),
    (r"0[,.]70?\s*L\b|70\s*cl\b", "0,70 L"),
    (r"(?<![,.\d])1\s*L(T)?\b|100\s*cl\b", "1 L"),
)


def formato(nome):
    for pad, fmt in FORMATOS:
        if re.search(pad, nome, re.I):
            return fmt
    return "0,75 L"


def col_index(ref):
    letras = re.sub(r"\d", "", ref or "").upper()
    n = 0
    for ch in letras:
        n = n * 26 + ord(ch) - 64
    return n - 1 if letras else None


def ler_xlsx(caminho):
    """Leitor mínimo de .xlsx só com a biblioteca padrão (primeira folha).

    Respeita a posição das colunas (células vazias omitidas no XML não encostam as colunas).
    """
    with zipfile.ZipFile(caminho) as z:
        partilhadas = []
        if "xl/sharedStrings.xml" in z.namelist():
            raiz = ET.fromstring(z.read("xl/sharedStrings.xml"))
            for si in raiz.findall("m:si", NS):
                partilhadas.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
        folhas = sorted(n for n in z.namelist() if re.match(r"xl/worksheets/sheet\d+\.xml", n))
        raiz = ET.fromstring(z.read(folhas[0]))
    linhas = []
    for row in raiz.iter("{%s}row" % NS["m"]):
        valores = {}
        for pos, c in enumerate(row.findall("m:c", NS)):
            col = col_index(c.get("r"))
            col = pos if col is None else col
            v = c.find("m:v", NS)
            if c.get("t") == "s" and v is not None:
                txt = partilhadas[int(v.text)]
            elif c.get("t") == "inlineStr":
                txt = "".join(t.text or "" for t in c.iter("{%s}t" % NS["m"]))
            else:
                txt = v.text if v is not None else ""
            valores[col] = txt
        if valores:
            linhas.append([valores.get(i, "") for i in range(max(valores) + 1)])
    return linhas


def ler_tabela(caminho):
    baixo = caminho.lower()
    if baixo.endswith((".xls", ".ods")):
        sys.exit("Formato não suportado: exporta do Odoo em .xlsx ou .csv.")
    if baixo.endswith(".xlsx"):
        return ler_xlsx(caminho)
    with open(caminho, encoding="utf-8-sig") as f:
        amostra = f.read(4096)
        f.seek(0)
        delim = "\t" if baixo.endswith(".tsv") or amostra.count("\t") > amostra.count(",") else ","
        if delim == "," and amostra.count(";") > amostra.count(","):
            delim = ";"
        return list(csv.reader(f, delimiter=delim))


def num(v):
    s = re.sub(r"[€\s\xa0]", "", str(v or ""))
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".") if s.rfind(",") > s.rfind(".") else s.replace(",", "")
    else:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("ficheiro")
    p.add_argument("--data", default=datetime.date.today().isoformat(), help="data da exportação (AAAA-MM-DD)")
    p.add_argument("--sem-destilados", action="store_true", help="não incluir a categoria Liquori e distillati")
    a = p.parse_args()

    linhas = ler_tabela(a.ficheiro)
    cab_idx = next((i for i, l in enumerate(linhas) if l and l[0].strip() == "Produto"), None)
    if cab_idx is None:
        sys.exit("Não encontrei a linha de cabeçalho com 'Produto' na primeira coluna.")
    cab = [c.strip() for c in linhas[cab_idx]]
    idx = {nome: cab.index(nome) for nome in cab if nome}
    obrig = ["Produto", "Categoria de Artigo", "Quantidade Em Mão", "Preço de Vendas"]
    falta = [c for c in obrig if c not in idx]
    if falta:
        sys.exit(f"Colunas em falta: {falta}")

    antigos = {}
    if os.path.exists(PRECOS):
        with open(PRECOS, encoding="utf-8-sig") as f:
            antigos = {r["sku"]: r for r in csv.DictReader(f)}

    cats = set(CATEGORIAS_VINHO) | (set() if a.sem_destilados else CATEGORIAS_DESTILADOS)
    por_sku, sem_sku, ilegiveis, negativos = {}, [], [], []
    for l in linhas[cab_idx + 1:]:
        l = l + [""] * (len(cab) - len(l))
        cat = l[idx["Categoria de Artigo"]].strip().split("/")[-1].strip()   # 'All / Vini' -> 'Vini'
        if cat.lower() not in cats:
            continue
        produto = l[idx["Produto"]].strip()
        m = re.match(r"\[([^\]]+)\]\s*(.*)", produto)
        if not m:
            sem_sku.append(produto)
            continue
        sku, nome = m.group(1).strip(), m.group(2).strip()
        preco = num(l[idx["Preço de Vendas"]])
        if preco is None:
            ilegiveis.append(sku)
        stock = num(l[idx["Quantidade Em Mão"]]) or 0
        if stock < 0:
            negativos.append(f"{sku} ({stock:.0f})")
            stock = 0
        chegar = num(l[idx["A Chegar"]]) if "A Chegar" in idx else 0
        r = por_sku.get(sku)
        if r:   # SKU repetido: soma stock e a chegar
            r["_stock"] += stock
            r["_chegar"] += chegar or 0
            continue
        fmt = formato(nome)
        if sku in antigos and fmt == "0,75 L" and antigos[sku].get("formato") not in ("", "0,75 L"):
            fmt = antigos[sku]["formato"]
        por_sku[sku] = {"sku": sku, "nome_odoo": nome, "categoria": cat, "formato": fmt,
                        "_stock": stock, "_chegar": chegar or 0, "_preco": preco}

    if not any(r["categoria"].lower() in CATEGORIAS_VINHO for r in por_sku.values()):
        sys.exit("Nenhum artigo da categoria Vini na exportação: nada foi gravado. "
                 "Confirma o ficheiro e a coluna 'Categoria de Artigo'.")

    saida = []
    for sku, r in por_sku.items():
        ant = antigos.get(sku, {})
        preco = r["_preco"]
        data = a.data
        if (preco or 0) <= 1.0 and (num(ant.get("preco_trade_eur")) or 0) > 1.0:
            preco = num(ant["preco_trade_eur"])        # marcador 1,00 não apaga um preço real anterior
            data = f"{a.data} (preço de {ant.get('data', '?')})"
        saida.append({
            "sku": sku, "nome_odoo": r["nome_odoo"], "categoria": r["categoria"], "formato": r["formato"],
            "stock": f"{r['_stock']:.0f}", "a_chegar": f"{r['_chegar']:.0f}",
            "preco_trade_eur": "" if preco is None else f"{preco:.2f}",
            "preco_trade_eur_2024h2": ant.get("preco_trade_eur_2024h2", ""), "data": data,
        })
    novos_skus = set(por_sku)
    # SKUs antigos ausentes desta exportação: mantêm o último preço, sem stock, marcados para revisão
    for sku, r in antigos.items():
        if sku in novos_skus:
            continue
        r = {k: r.get(k, "") for k in CAMPOS}
        r["stock"] = ""
        r["a_chegar"] = ""
        r["data"] = re.sub(r"; ausente na exportação .*$", "", r.get("data", "")) + f"; ausente na exportação {a.data}"
        saida.append(r)

    os.makedirs(os.path.dirname(PRECOS), exist_ok=True)
    if os.path.exists(PRECOS):
        shutil.copyfile(PRECOS, BACKUP)
    with open(PRECOS, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(saida)
    n_vinho = sum(1 for r in por_sku.values() if r["categoria"].lower() in CATEGORIAS_VINHO)
    print(f"Gravadas {len(saida)} linhas em {PRECOS} (data {a.data}): {n_vinho} vinhos e "
          f"{len(por_sku) - n_vinho} destilados desta exportação, {len(saida) - len(por_sku)} SKUs antigos mantidos.")
    if os.path.exists(BACKUP):
        print(f"Cópia da versão anterior: {BACKUP}")
    if sem_sku:
        print(f"\nAviso: {len(sem_sku)} artigo(s) sem [referência] no nome, ignorados: " + "; ".join(sem_sku[:5]))
    if ilegiveis:
        print(f"\nAviso: preço ilegível em {len(ilegiveis)} SKU(s): " + ", ".join(ilegiveis[:10]))
    if negativos:
        print(f"\nAviso: stock negativo no Odoo, gravado como 0: " + ", ".join(negativos[:10]))

    if os.path.exists(CATALOGO):
        with open(CATALOGO, encoding="utf-8") as f:
            cat = json.load(f)
        conhecidos = {s for v in cat["vinhos"] for s in v.get("skus", [])}
        novos = [r for s, r in por_sku.items() if s not in conhecidos and r["categoria"].lower() in CATEGORIAS_VINHO]
        ausentes = [v for v in cat["vinhos"] if v.get("skus") and not (set(v["skus"]) & novos_skus)
                    and v.get("estado") != "descontinuado"]
        if novos:
            print(f"\n{len(novos)} artigo(s) de vinho novos, sem ficha no catálogo (pesquisar e acrescentar):")
            for r in novos:
                print(f"  [{r['sku']}] {r['nome_odoo']}  stock={r['_stock']:.0f}")
        if ausentes:
            print(f"\n{len(ausentes)} vinho(s) do catálogo sem nenhum SKU nesta exportação (rever estado):")
            for v in ausentes:
                print(f"  {v['produtor']} - {v['nome']} ({', '.join(v['skus'])})")


if __name__ == "__main__":
    main()
