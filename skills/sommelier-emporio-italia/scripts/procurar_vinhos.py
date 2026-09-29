#!/usr/bin/env python3
"""Procura vinhos no catálogo Emporio Italia.

Lê data/catalogo.json (público) e, se existir, data/precos_stock.csv (privado:
preço trade sem IVA e stock por SKU). Sem dependências externas.

Exemplos:
  python3 scripts/procurar_vinhos.py --resumo
  python3 scripts/procurar_vinhos.py --tipo tinto --regiao piemonte
  python3 scripts/procurar_vinhos.py --harmoniza polvo
  python3 scripts/procurar_vinhos.py --denominacao barolo --preco-max 30 --por-sku
  python3 scripts/procurar_vinhos.py --casta nebbiolo --com-stock
  python3 scripts/procurar_vinhos.py --texto etna --formato json
  python3 scripts/procurar_vinhos.py --estado todos --produtor pasqua

Vista por vinho (defeito): uma linha por vinho, com o preço de referência da
garrafa de 0,75 L e o stock total de todos os formatos e colheitas.
Vista por SKU (--por-sku): uma linha por SKU (colheita, formato, preço, stock).
Use-a sempre que for propor preços: os filtros de preço e stock passam a ser
aplicados SKU a SKU.
"""
import argparse
import csv
import json
import os
import re
import sys
import unicodedata

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOGO = os.path.join(BASE, "data", "catalogo.json")
PRECOS = os.path.join(BASE, "data", "precos_stock.csv")

ESTADOS_ATIVOS = {"ativo_com_stock", "ativo_sem_stock"}
ORDEM_TIPO = ["espumante", "frisante", "branco", "rose", "tinto", "doce", "cocktail"]
GARRAFA = "0,75 L"
REGIOES_PT = {"sardenha": "sardegna", "apulia": "puglia", "emilia-romanha": "emilia-romagna",
              "emilia romanha": "emilia-romagna", "abruzos": "abruzzo", "lacio": "lazio", "marcas": "marche",
              "sicilia": "sicilia", "toscania": "toscana", "venecia": "veneto", "lombardia": "lombardia"}


def norm(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode()
    return s.lower()


def num(v):
    try:
        return float(str(v).replace(",", "."))
    except (TypeError, ValueError):
        return None


def preco_real(v):
    """Preços 0,00 e 1,00 são marcadores do Odoo, não preços reais."""
    p = num(v)
    return p if p is not None and p > 1.0 else None


def colheita(nome, sku=""):
    m = re.search(r"\b(19[89]\d|20[0-3]\d)\b", nome or "")
    if m:
        return m.group(1)
    m = re.search(r"[-_](20[0-3]\d|[0-3]\d)$", sku or "")
    if not m:
        return ""
    ano = m.group(1) if len(m.group(1)) == 4 else "20" + m.group(1)
    return ano + " (pelo SKU)"


def carregar_precos():
    if not os.path.exists(PRECOS):
        return {}
    with open(PRECOS, encoding="utf-8-sig") as f:
        return {r["sku"].strip(): r for r in csv.DictReader(f)}


def linhas_sku(vinho, precos):
    """Uma linha por SKU do vinho, com preço atual (ou de 2024, marcado) e stock."""
    out = []
    for s in vinho.get("skus", []):
        r = precos.get(s)
        if not r:
            continue
        p26 = preco_real(r.get("preco_trade_eur"))
        p24 = preco_real(r.get("preco_trade_eur_2024h2"))
        stock = num(r.get("stock")) if (r.get("stock") or "") != "" else None
        out.append({
            "sku": s,
            "nome_odoo": r.get("nome_odoo", ""),
            "colheita": colheita(r.get("nome_odoo", ""), s),
            "formato": r.get("formato", GARRAFA),
            "preco": p26 if p26 is not None else p24,
            "preco_fonte": "odoo" if p26 is not None else ("lista 2024-H2" if p24 is not None else ""),
            "stock": stock,
            "data": r.get("data", ""),
        })
    return out


def enriquecer(vinho, precos):
    v = dict(vinho)
    ls = linhas_sku(vinho, precos)
    v["_skus"] = ls
    stocks = [max(l["stock"], 0) for l in ls if l["stock"] is not None]
    v["_stock"] = sum(stocks) if stocks else None
    st_g = [max(l["stock"], 0) for l in ls if l["stock"] is not None and l["formato"] == GARRAFA]
    v["_stock_garrafa"] = sum(st_g) if st_g else None
    # preço de referência: garrafa 0,75 L; preço Odoo primeiro, 2024 só se não houver
    ref = None
    for fonte in ("odoo", "lista 2024-H2"):
        cands = [l for l in ls if l["formato"] == GARRAFA and l["preco_fonte"] == fonte]
        if cands:
            # com stock primeiro, depois o mais barato
            cands.sort(key=lambda l: (not (l["stock"] or 0) > 0, l["preco"]))
            ref = cands[0]
            break
    v["_preco"] = ref["preco"] if ref else None
    v["_preco_fonte"] = ref["preco_fonte"] if ref else ""
    return v


def relevancia(v, termo):
    t = norm(termo)
    pontos = 0
    for campo, peso in (("harmonizacoes_pt", 3), ("harmonizacoes", 2), ("harmonizacoes_menu_emporio", 1)):
        for h in v.get(campo) or []:
            nh = norm(h)
            if t in nh:
                pontos += peso
                if nh.startswith(t) or nh == t:
                    pontos += peso   # o prato pedido, não um prato vizinho (ex.: 'salada de polvo')
    return pontos


def filtrar(vinhos, a):
    out = []
    for v in vinhos:
        if a.tipo and norm(v.get("tipo")) != norm(a.tipo):
            continue
        reg = REGIOES_PT.get(norm(a.regiao), norm(a.regiao)) if a.regiao else ""
        if reg and reg not in norm(v.get("regiao")) and reg not in norm(v.get("regiao_base")):
            continue
        if a.casta and norm(a.casta) not in norm(v.get("castas")):
            continue
        if a.produtor and norm(a.produtor) not in norm(v.get("produtor")):
            continue
        if a.denominacao and norm(a.denominacao) not in norm(v.get("denominacao")):
            continue
        if a.classificacao and norm(a.classificacao) != norm(v.get("classificacao")):
            continue
        if a.harmoniza:
            v["_relevancia"] = relevancia(v, a.harmoniza)
            if not v["_relevancia"]:
                continue
        if a.texto:
            blob = norm(" ".join(json.dumps(x, ensure_ascii=False) for k, x in v.items()
                                 if not k.startswith("_") and k not in ("fontes", "id", "ficha")))
            if norm(a.texto) not in blob:
                continue
        if a.estado == "ativo" and v.get("estado") not in ESTADOS_ATIVOS:
            continue
        if a.estado == "propor" and v.get("estado") not in ESTADOS_ATIVOS | {"nao_confirmado_2026"}:
            continue
        if a.estado not in (None, "ativo", "propor", "todos") and v.get("estado") != a.estado:
            continue
        if a.corpo_min and (v.get("corpo") or 0) < a.corpo_min:
            continue
        if a.corpo_max and (v.get("corpo") or 9) > a.corpo_max:
            continue
        if a.por_sku:
            # na vista por SKU o vinho fica se pelo menos um SKU passar os filtros de preço/stock
            if (a.com_stock or a.preco_max is not None or a.preco_min is not None or a.so_garrafa) and not skus_filtrados(v, a):
                continue
        else:
            if a.com_stock and not (v.get("_stock_garrafa") if v.get("_stock_garrafa") is not None else v.get("_stock") or 0) > 0:
                continue
            if a.preco_max is not None and (v["_preco"] is None or v["_preco"] > a.preco_max):
                continue
            if a.preco_min is not None and (v["_preco"] is None or v["_preco"] < a.preco_min):
                continue
        out.append(v)

    def chave_base(v):
        return (ORDEM_TIPO.index(v["tipo"]) if v.get("tipo") in ORDEM_TIPO else 99,
                v.get("_preco") or 9999, v.get("produtor") or "", v.get("nome") or "")

    if a.harmoniza:
        out.sort(key=lambda v: (-v.get("_relevancia", 0),) + chave_base(v))
    else:
        out.sort(key=chave_base)
    return out


def skus_filtrados(v, a):
    res = []
    for l in v["_skus"]:
        if a.com_stock and not (l["stock"] or 0) > 0:
            continue
        if a.preco_max is not None and (l["preco"] is None or l["preco"] > a.preco_max):
            continue
        if a.preco_min is not None and (l["preco"] is None or l["preco"] < a.preco_min):
            continue
        if a.so_garrafa and l["formato"] != GARRAFA:
            continue
        res.append(l)
    return res


def celula(x):
    return str(x if x is not None else "").replace("|", "/").replace("\n", " ")


def tabela_vinhos(vinhos, tem_precos):
    cab = ["Produtor", "Vinho", "Denominação", "Tipo", "Castas", "Estado", "Gama"]
    if tem_precos:
        cab += ["Trade € (0,75 L)", "Stock 0,75 L", "Stock total"]
    linhas = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    for v in vinhos:
        row = [v.get("produtor"), v.get("nome"), v.get("denominacao"), v.get("tipo"),
               (v.get("castas") or "")[:60], v.get("estado"), v.get("gama_preco")]
        if tem_precos:
            ref = "" if v["_preco"] is None else f"{v['_preco']:.2f}"
            if ref and v["_preco_fonte"] == "lista 2024-H2":
                ref += " (2024)"
            row += [ref, "" if v["_stock_garrafa"] is None else f"{v['_stock_garrafa']:.0f}",
                    "" if v["_stock"] is None else f"{v['_stock']:.0f}"]
        linhas.append("| " + " | ".join(celula(c) for c in row) + " |")
    return "\n".join(linhas)


def tabela_skus(vinhos, a):
    cab = ["Produtor", "Vinho", "Estado", "SKU", "Colheita", "Formato", "Trade €", "Stock", "Data"]
    linhas = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    n = 0
    for v in vinhos:
        for l in skus_filtrados(v, a):
            preco = "" if l["preco"] is None else f"{l['preco']:.2f}"
            if preco and l["preco_fonte"] == "lista 2024-H2":
                preco += " (2024)"
            linhas.append("| " + " | ".join(celula(c) for c in (
                v.get("produtor"), v.get("nome"), v.get("estado"),
                l["sku"].replace("#2024b", "#2024").replace("#2024", " (código da lista 2024, hoje de outro artigo)"),
                l["colheita"], l["formato"], preco,
                "" if l["stock"] is None else f"{l['stock']:.0f}", l["data"])) + " |")
            n += 1
    return n, "\n".join(linhas)


def resumo(vinhos):
    from collections import Counter
    print(f"Total de vinhos no catálogo: {len(vinhos)}")
    for campo in ("estado", "tipo", "regiao_base", "classificacao"):
        print(f"\nPor {campo}:")
        for k, n in Counter(v.get(campo) or "?" for v in vinhos).most_common():
            print(f"  {k}: {n}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--tipo", choices=ORDEM_TIPO)
    p.add_argument("--regiao")
    p.add_argument("--casta")
    p.add_argument("--produtor")
    p.add_argument("--denominacao")
    p.add_argument("--classificacao", help="DOCG, DOC, IGT...")
    p.add_argument("--harmoniza", help="palavra de um prato: polvo, bacalhau, tartufo, pizza... (ordena por relevância)")
    p.add_argument("--texto", help="pesquisa livre em todos os campos")
    p.add_argument("--estado", default="ativo",
                   choices=["ativo", "propor", "todos", "ativo_com_stock", "ativo_sem_stock", "nao_confirmado_2026", "descontinuado"],
                   help="ativo (defeito: com e sem stock), propor (ativos + nao_confirmado_2026), todos, ou um estado")
    p.add_argument("--corpo-min", type=int)
    p.add_argument("--corpo-max", type=int)
    p.add_argument("--preco-max", type=float, help="preço trade máximo em € sem IVA (requer ficheiro privado)")
    p.add_argument("--preco-min", type=float)
    p.add_argument("--com-stock", action="store_true", help="só com stock (requer ficheiro privado)")
    p.add_argument("--por-sku", action="store_true", help="uma linha por SKU (colheita, formato, preço, stock)")
    p.add_argument("--so-garrafa", action="store_true", help="só com --por-sku: só garrafas de 0,75 L")
    p.add_argument("--formato", choices=["tabela", "json"], default="tabela")
    p.add_argument("--resumo", action="store_true", help="estatísticas de todo o catálogo (ignora os outros filtros)")
    a = p.parse_args()

    if not os.path.exists(CATALOGO):
        sys.exit(f"Catálogo não encontrado: {CATALOGO}")
    with open(CATALOGO, encoding="utf-8") as f:
        cat = json.load(f)
    precos = carregar_precos()
    vinhos = [enriquecer(v, precos) for v in cat["vinhos"]]

    if a.resumo:
        resumo(vinhos)
        if not precos:
            print("\n(Ficheiro privado de preços/stock ausente: data/precos_stock.csv)")
        return
    if (a.preco_max is not None or a.preco_min is not None or a.com_stock or a.por_sku) and not precos:
        print("AVISO: data/precos_stock.csv não existe. --com-stock passa a usar o estado ativo_com_stock "
              "(20/02/2026) e --preco-max/--preco-min passam a usar a gama (€ a €€€€€). Preços por confirmar.\n")
        limites = {"€": (0, 6), "€€": (6, 12), "€€€": (12, 25), "€€€€": (25, 50), "€€€€€": (50, 1e9)}
        pmax, pmin = a.preco_max, a.preco_min
        if pmax is not None or pmin is not None:
            vinhos = [v for v in vinhos if v.get("gama_preco") in limites
                      and (pmax is None or limites[v["gama_preco"]][0] < pmax)
                      and (pmin is None or limites[v["gama_preco"]][1] > pmin)]
        if a.com_stock:
            vinhos = [v for v in vinhos if v.get("estado") == "ativo_com_stock"]
        a.preco_max = a.preco_min = None
        a.com_stock = a.por_sku = False

    res = filtrar(vinhos, a)
    if a.formato == "json":
        if a.por_sku:
            for v in res:
                v["_skus"] = skus_filtrados(v, a)
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return
    if a.por_sku:
        n, t = tabela_skus(res, a)
        print(f"{n} SKU(s) de {len(res)} vinho(s)\n")
        print(t)
    else:
        print(f"{len(res)} vinho(s)\n")
        print(tabela_vinhos(res, bool(precos)))
    if precos:
        mostradas = (lambda v: skus_filtrados(v, a)) if a.por_sku else (lambda v: v["_skus"])
        datas = sorted({l["data"] for v in res for l in mostradas(v) if l["data"]})
        print("\nPreços trade sem IVA e stock do ficheiro privado. Datas dos dados: "
              + ("; ".join(datas) if datas else "?") + ". Confirmar sempre no Odoo antes de propor.")


if __name__ == "__main__":
    main()
