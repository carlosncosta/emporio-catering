#!/usr/bin/env python3
"""Calcula preços de carta sugeridos (garrafa e copo) a partir do preço trade Emporio.

Segue references/conhecimento/servico-e-carta-de-vinhos.md, secções 12.5 e 13.2:
- multiplicador decrescente por patamar de custo (valores indicativos da referência,
  usa-se o ponto médio de cada intervalo; pode ser alterado com --mult);
- IVA de 23 % sobre o vinho servido na restauração (continente; confirmar sempre);
- garrafa arredondada ao euro; copo arredondado a 0,50 €;
- copo: custo por copo real × (multiplicador da garrafa × 1,2), o que reproduz o
  exemplo da referência (garrafa × 2,5 → copo × 3,0).

Os preços finais são decisão do cliente: apresentar sempre como sugestão.

Uso:
  python3 scripts/precos_carta.py 6002A005 6006A015:copo 6024A003
  python3 scripts/precos_carta.py 6002A005 6004A002-1:copo --dose 12.5 --teto 45 --piso 20
  python3 scripts/precos_carta.py 6002A005 --mult 2.5            (multiplicador fixo)
  python3 scripts/precos_carta.py 6002A005 --iva 22              (Madeira/Açores: confirmar a taxa)
"""
import argparse
import math
import csv
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOGO = os.path.join(BASE, "data", "catalogo.json")
PRECOS = os.path.join(BASE, "data", "precos_stock.csv")

# (limite superior do custo, multiplicador = ponto médio do intervalo da secção 13.2)
PATAMARES = [(5, 3.25), (10, 2.75), (20, 2.35), (40, 2.0), (float("inf"), 1.65)]
COPOS_REAIS = {15.0: 5.0, 12.5: 5.7}


def num(v):
    try:
        return float(str(v).replace(",", "."))
    except (TypeError, ValueError):
        return None


def multiplicador(custo):
    for lim, m in PATAMARES:
        if custo <= lim:
            return m
    return PATAMARES[-1][1]


def arred(x, passo):
    return math.floor(x / passo + 0.5) * passo   # meio sempre para cima


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("skus", nargs="+", help="SKU, ou SKU:copo para incluir o preço a copo")
    p.add_argument("--mult", type=float, help="multiplicador fixo para todas as garrafas")
    p.add_argument("--iva", type=float, default=23.0, help="taxa de IVA em %% (defeito 23, continente)")
    p.add_argument("--dose", type=float, default=15.0, choices=[15.0, 12.5], help="dose do copo em cl")
    p.add_argument("--teto", type=float, help="PVP máximo pretendido na carta (€)")
    p.add_argument("--piso", type=float, help="PVP mínimo pretendido na carta (€)")
    p.add_argument("--stock-min", type=float, default=36, help="alerta se stock abaixo disto (defeito 36)")
    a = p.parse_args()

    if not os.path.exists(PRECOS):
        sys.exit("data/precos_stock.csv (privado) não existe: sem preços trade não é possível calcular.")
    with open(PRECOS, encoding="utf-8-sig") as f:
        precos = {r["sku"].strip(): r for r in csv.DictReader(f)}
    nomes = {}
    if os.path.exists(CATALOGO):
        with open(CATALOGO, encoding="utf-8") as f:
            for v in json.load(f)["vinhos"]:
                for s in v.get("skus", []):
                    nomes[s] = (v.get("produtor", ""), v.get("nome", ""), v.get("estado", ""))

    fator_iva = 1 + a.iva / 100
    copos = COPOS_REAIS[a.dose]
    print(f"IVA {a.iva:.0f} % · copo de {a.dose:g} cl com {copos:g} copos reais por garrafa · "
          f"multiplicador {'fixo ' + str(a.mult) if a.mult else 'escalonado (secção 13.2)'}\n")
    cab = ["SKU", "Vinho", "Colheita", "Formato", "Trade €", "Stock", "M", "Carta garrafa €",
           "Margem restaurante €/garrafa", "Copo €", "Copos vs garrafa", "Alertas"]
    print("| " + " | ".join(cab) + " |")
    print("|" + "---|" * len(cab))
    total_margem = 0.0
    for arg in a.skus:
        sku, _, flag = arg.partition(":")
        r = precos.get(sku)
        alertas = []
        if not r:
            print(f"| {sku} | (SKU não encontrado no ficheiro de preços) |" + " |" * (len(cab) - 2))
            continue
        custo = num(r.get("preco_trade_eur"))
        fonte = "odoo"
        if not custo or custo <= 1.0:
            custo = num(r.get("preco_trade_eur_2024h2"))
            fonte = "2024"
            alertas.append("preço da lista 2024: confirmar")
        if not custo or custo <= 1.0:
            print(f"| {sku} | {r.get('nome_odoo', '')} | sem preço real |" + " |" * (len(cab) - 3))
            continue
        m = a.mult or multiplicador(custo)
        pvp_sem = custo * m
        carta = arred(pvp_sem * fator_iva, 1.0)
        margem = carta / fator_iva - custo
        total_margem += margem
        copo_txt = rend_txt = ""
        if flag.lower().startswith("copo") and r.get("formato", "0,75 L") != "0,75 L":
            alertas.append("copo só se calcula para garrafas de 0,75 L")
        elif flag.lower().startswith("copo"):
            copo = arred(custo / copos * m * 1.2 * fator_iva, 0.5)
            copo_txt = f"{copo:.2f}"
            rend = copo * copos / carta - 1
            rend_txt = f"{rend:+.0%}"
            if rend < 0.15 or rend > 0.35:
                alertas.append("rendimento do copo fora de 15-35 %")
        stock = num(r.get("stock"))
        if stock is None:
            alertas.append("sem stock conhecido")
        elif stock <= 0:
            alertas.append("sem stock")
        elif stock < a.stock_min:
            alertas.append(f"stock baixo ({stock:.0f})")
        if r.get("formato") and r["formato"] != "0,75 L":
            alertas.append(f"formato {r['formato']}")
        if a.teto and carta > a.teto:
            alertas.append(f"acima do teto {a.teto:g} €")
        if a.piso and carta < a.piso:
            alertas.append(f"abaixo do piso {a.piso:g} €")
        if "#" in sku:
            alertas.append("código da lista 2024, hoje de outro artigo: não usar em encomendas")
        prod, nome, estado = nomes.get(sku, ("", r.get("nome_odoo", ""), ""))
        if estado and estado not in ("ativo_com_stock", "ativo_sem_stock"):
            alertas.append(estado)
        m_col = re.search(r"\b(19[89]\d|20[0-3]\d)\b", r.get("nome_odoo", ""))
        print("| " + " | ".join(str(x) for x in (
            sku, f"{prod} {nome}".strip(), m_col.group(1) if m_col else "a confirmar", r.get("formato", ""),
            f"{custo:.2f}" + (" (2024)" if fonte == "2024" else ""), "" if stock is None else f"{stock:.0f}",
            f"{m:.2f}", f"{carta:.0f}", f"{margem:.2f}", copo_txt, rend_txt, "; ".join(alertas))) + " |")
    print(f"\nMargem bruta do restaurante somada (1 garrafa de cada, sem IVA): {total_margem:.2f} €")
    print(f"Dados: {PRECOS} (datas na coluna 'data'). Multiplicadores indicativos, não verificados: "
          "são sugestões, o preço final é do cliente. Confirmar a taxa de IVA em vigor.")


if __name__ == "__main__":
    main()
