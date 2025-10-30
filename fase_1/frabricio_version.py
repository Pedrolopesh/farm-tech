# -*- coding: utf-8 -*-
"""
Programa Único — Sistema Agrícola (Completo, sem bibliotecas externas)
Funcionalidades:
- Gera dataset CSV (MT 2010–2024) se não existir (Soja/Milho; NA onde faltar)
- Lê CSV e calcula estatísticas simples (sem pandas)
- CRUD de Talhões com persistência em JSON
- Cálculo de áreas (quadrado, retângulo, círculo)
- Cálculo de insumos (por ha e por metro)
- Exporta relatórios (JSON/CSV)

Dica: se a sua IDE online derrubar por inatividade, use o modo DEMO no final.
"""
import os, json, csv, math
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

# ------------------------------------------------------------
# Config e Paths
# ------------------------------------------------------------
BASE = Path("..").resolve()
DATA = BASE / "data"
DOCS = BASE / "docs"
for p in (DATA, DOCS):
    p.mkdir(parents=True, exist_ok=True)

CSV_MT = DATA / "dados_agricolas_mt_2010_2024.csv"
ARQ_TALHOES = DATA / "talhoes.json"
EXP_JSON = DOCS / "export_talhoes.json"
EXP_CSV = DOCS / "export_talhoes.csv"

M2_POR_HA = 10_000.0

# ------------------------------------------------------------
# Utilitários
# ------------------------------------------------------------
def agora_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")

def to_float_or_none(s: str) -> Optional[float]:
    if s is None: return None
    s = str(s).strip().replace(",", ".")
    if s.upper() == "NA" or s == "": return None
    try:
        return float(s)
    except:
        return None

# ------------------------------------------------------------
# Dataset base (Etapa 1) — criar se não existir
# ------------------------------------------------------------
def garantir_csv_mt():
    if CSV_MT.exists():
        return
    years = range(2010, 2025)
    culturas = ["Soja", "Milho"]
    campos = ["ano","cultura","area_ha","producao_t","produtividade_t_ha","preco_rs","exportacao_t"]
    with CSV_MT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for ano in years:
            for cultura in culturas:
                w.writerow({
                    "ano": ano,
                    "cultura": cultura,
                    "area_ha": "NA",
                    "producao_t": "NA",
                    "produtividade_t_ha": "NA",
                    "preco_rs": "NA",
                    "exportacao_t": "NA",
                })

# ------------------------------------------------------------
# Estatísticas simples do CSV (sem pandas) — Etapa 6 (alternativa)
# ------------------------------------------------------------
def ler_csv_mt() -> List[Dict[str, Any]]:
    rows = []
    if not CSV_MT.exists():
        return rows
    with CSV_MT.open("r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            rows.append(row)
    return rows

def stats_basicas(rows: List[Dict[str, Any]]):
    """Computa count, média e soma para algumas colunas numéricas, ignorando NA."""
    def colnums(nome: str):
        vals = []
        for row in rows:
            v = to_float_or_none(row.get(nome))
            if v is not None:
                vals.append(v)
        return vals

    def resumo(nome: str):
        xs = colnums(nome)
        n = len(xs)
        total = sum(xs) if n else 0.0
        media = (total / n) if n else 0.0
        return {"coluna": nome, "n": n, "soma": total, "media": media}

    colunas = ["area_ha","producao_t","produtividade_t_ha","preco_rs","exportacao_t"]
    return [resumo(c) for c in colunas]

def stats_por_cultura(rows: List[Dict[str, Any]]):
    """Médias por cultura para colunas numéricas."""
    grupos: Dict[str, Dict[str, List[float]]] = {}
    colunas = ["area_ha","producao_t","produtividade_t_ha","preco_rs","exportacao_t"]
    for row in rows:
        cult = row.get("cultura","?")
        g = grupos.setdefault(cult, {c: [] for c in colunas})
        for c in colunas:
            v = to_float_or_none(row.get(c))
            if v is not None:
                g[c].append(v)
    medias = {}
    for cult, d in grupos.items():
        medias[cult] = {}
        for c, arr in d.items():
            medias[cult][c] = (sum(arr)/len(arr)) if arr else 0.0
    return medias

def mostrar_stats_csv():
    rows = ler_csv_mt()
    if not rows:
        print("⚠️ CSV não encontrado.")
        return
    print("\n=== Estatísticas (CSV MT 2010–2024) — gerais ===")
    for s in stats_basicas(rows):
        print(f"- {s['coluna']}: n={s['n']} | soma={s['soma']:.2f} | média={s['media']:.2f}")
    print("\n=== Estatísticas por cultura (médias) ===")
    medias = stats_por_cultura(rows)
    for cult, d in medias.items():
        print(f"[{cult}] ", end="")
        print(" | ".join(f"{k}={v:.2f}" for k,v in d.items()))

# ------------------------------------------------------------
# Modelo/Talhão + Persistência — Etapas 2, 4, 5
# ------------------------------------------------------------
@dataclass
class Talhao:
    id: int
    nome: str
    cultura: str
    area_ha: float
    criado_em: str
    atualizado_em: str

def carregar_talhoes() -> List[Talhao]:
    if not ARQ_TALHOES.exists():
        return []
    try:
        data = json.loads(ARQ_TALHOES.read_text(encoding="utf-8"))
        return [Talhao(**t) for t in data.get("talhoes", [])]
    except Exception as e:
        print(f"ERRO ao carregar talhões: {e}")
        return []

def salvar_talhoes(talhoes: List[Talhao]) -> None:
    payload = {"talhoes": [asdict(t) for t in talhoes]}
    ARQ_TALHOES.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

def next_id(talhoes: List[Talhao]) -> int:
    return max([t.id for t in talhoes], default=0) + 1

# ------------------------------------------------------------
# Cálculo de áreas — Etapa 2
# ------------------------------------------------------------
def area_quadrado(lado_m: float) -> float:
    return (lado_m ** 2) / M2_POR_HA

def area_retangulo(largura_m: float, comprimento_m: float) -> float:
    return (largura_m * comprimento_m) / M2_POR_HA

def area_circulo(raio_m: float) -> float:
    return (math.pi * (raio_m ** 2)) / M2_POR_HA

def calcular_area_interativo(nome_cultura: str) -> float:
    print(f"\n=== Cálculo de área — {nome_cultura} ===")
    print("Formatos: [1] quadrado  [2] retângulo  [3] círculo")
    f = input("Escolha (1/2/3): ").strip()
    try:
        if f == "1":
            lado = float(input("Lado (m): ").replace(",", "."))
            a = area_quadrado(lado)
        elif f == "2":
            L = float(input("Largura (m): ").replace(",", "."))
            C = float(input("Comprimento (m): ").replace(",", "."))
            a = area_retangulo(L, C)
        elif f == "3":
            r = float(input("Raio (m): ").replace(",", "."))
            a = area_circulo(r)
        else:
            raise ValueError
        print(f"Área: {a:.4f} ha")
        return a
    except Exception:
        print("Entrada inválida.")
        return 0.0

# ------------------------------------------------------------
# Manejo de insumos — Etapa 3
# ------------------------------------------------------------
def calcular_insumo_area(cultura: str, produto: str, area_ha: float, dose_por_ha: float) -> float:
    if area_ha <= 0 or dose_por_ha <= 0:
        raise ValueError("Área e dose devem ser > 0.")
    total = area_ha * dose_por_ha
    print(f"{cultura} | {produto} = {total:.2f} (para {area_ha:.2f} ha, dose {dose_por_ha}/ha)")
    return total

def calcular_insumo_linhas(cultura: str, produto: str, num_linhas: int, comp_linha_m: float, dose_por_m: float) -> float:
    if num_linhas <= 0 or comp_linha_m <= 0 or dose_por_m <= 0:
        raise ValueError("Linhas, comprimento e dose devem ser > 0.")
    total_m = num_linhas * comp_linha_m
    total = total_m * dose_por_m
    print(f"{cultura} | {produto} = {total:.2f} (para {num_linhas} linhas x {comp_linha_m} m, dose {dose_por_m}/m)")
    return total

# ------------------------------------------------------------
# Exportações
# ------------------------------------------------------------
def exportar_json(talhoes: List[Talhao]) -> None:
    payload = {"exportado_em": agora_iso(), "talhoes": [asdict(t) for t in talhoes]}
    EXP_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Exportado JSON: {EXP_JSON}")

def exportar_csv(talhoes: List[Talhao]) -> None:
    campos = ["id","nome","cultura","area_ha","criado_em","atualizado_em"]
    with EXP_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos, delimiter=";")
        w.writeheader()
        for t in talhoes:
            w.writerow({k: getattr(t, k) for k in campos})
    print(f"✅ Exportado CSV: {EXP_CSV} (delimitador ';')")

# ------------------------------------------------------------
# Submenus
# ------------------------------------------------------------
def submenu_crud(talhoes: List[Talhao]) -> None:
    while True:
        print("\n--- CRUD Talhões ---")
        print("[1] Cadastrar")
        print("[2] Listar")
        print("[3] Excluir")
        print("[0] Voltar")
        op = input("Opção: ").strip()
        if op == "1":
            nome = input("Nome do talhão: ").strip() or f"T{next_id(talhoes)}"
            cultura = input("Cultura (Soja/Milho): ").strip() or "Soja"
            usar_calc = input("Calcular área agora? (s/n): ").strip().lower()
            if usar_calc == "s":
                area_ha = calcular_area_interativo(cultura)
            else:
                try:
                    area_ha = float(input("Área (ha): ").replace(",", "."))
                except:
                    print("Área inválida."); continue
            t = Talhao(
                id=next_id(talhoes),
                nome=nome, cultura=cultura, area_ha=area_ha,
                criado_em=agora_iso(), atualizado_em=agora_iso()
            )
            talhoes.append(t); salvar_talhoes(talhoes)
            print("✅ Cadastrado.")
        elif op == "2":
            if not talhoes: print("Sem talhões.")
            else:
                print("\nID | Nome | Cultura | Área(ha)")
                for t in talhoes:
                    print(f"{t.id:>2} | {t.nome} | {t.cultura} | {t.area_ha:.4f}")
        elif op == "3":
            if not talhoes: print("Sem talhões."); continue
            try:
                alvo = int(input("ID do talhão: ").strip())
            except:
                print("ID inválido."); continue
            antes = len(talhoes)
            talhoes[:] = [x for x in talhoes if x.id != alvo]
            if len(talhoes) < antes:
                salvar_talhoes(talhoes); print("🗑️ Excluído.")
            else:
                print("Não encontrado.")
        elif op == "0":
            return
        else:
            print("Opção inválida.")

def submenu_insumos() -> None:
    print("\n--- Manejo de Insumos ---")
    print("[1] Por hectare (dose/ha)")
    print("[2] Por linha (dose/m)")
    op = input("Opção: ").strip()
    cultura = input("Cultura: ").strip() or "Soja"
    produto = input("Produto/insumo: ").strip() or "Insumo"
    try:
        if op == "1":
            area = float(input("Área (ha): ").replace(",", "."))
            dose = float(input("Dose por ha: ").replace(",", "."))
            calcular_insumo_area(cultura, produto, area, dose)
        elif op == "2":
            linhas = int(input("Número de linhas: ").strip())
            comp = float(input("Comprimento por linha (m): ").replace(",", "."))
            dose_m = float(input("Dose por metro linear: ").replace(",", "."))
            calcular_insumo_linhas(cultura, produto, linhas, comp, dose_m)
        else:
            print("Opção inválida.")
    except ValueError as e:
        print(f"ERRO: {e}")

def submenu_dados_mt() -> None:
    print("\n--- Dados Agrícolas — MT (2010–2024) ---")
    if not CSV_MT.exists():
        print("CSV não encontrado.")
        return
    # Mostra as primeiras 12 linhas
    with CSV_MT.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            print(line.rstrip("\n"))
            if i >= 12: break
    mostrar_stats_csv()

def submenu_exportacoes(talhoes: List[Talhao]) -> None:
    print("\n--- Exportações ---")
    print("[1] Exportar JSON talhões")
    print("[2] Exportar CSV talhões")
    print("[0] Voltar")
    op = input("Opção: ").strip()
    if op == "1":
        exportar_json(talhoes)
    elif op == "2":
        exportar_csv(talhoes)
    elif op == "0":
        return
    else:
        print("Opção inválida.")

# ------------------------------------------------------------
# Menu principal
# ------------------------------------------------------------
def main():
    garantir_csv_mt()
    talhoes = carregar_talhoes()
    print("\n=== Sistema Agrícola — Programa Único ===")
    while True:
        print("\n[1] CRUD Talhões")
        print("[2] Cálculo de Áreas")
        print("[3] Manejo de Insumos")
        print("[4] Dados MT 2010–2024 (CSV + estatísticas)")
        print("[5] Exportações")
        print("[0] Sair")
        op = input("Escolha: ").strip()
        if op == "1":
            submenu_crud(talhoes)
        elif op == "2":
            c1 = input("Cultura: ").strip() or "Soja"
            calcular_area_interativo(c1)
        elif op == "3":
            submenu_insumos()
        elif op == "4":
            submenu_dados_mt()
        elif op == "5":
            submenu_exportacoes(talhoes)
        elif op == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

# ------------------------------------------------------------
# MODO DEMO (sem inputs) — útil em IDEs que expiram por inatividade
# ------------------------------------------------------------
def rodar_demo_rapida():
    garantir_csv_mt()
    # Estatísticas rápidas do CSV
    print("### DEMO: Estatísticas do CSV")
    mostrar_stats_csv()
    # Talhões de exemplo
    talhoes = [
        Talhao(1, "Soja A", "Soja", area_retangulo(100, 200), agora_iso(), agora_iso()),
        Talhao(2, "Milho B", "Milho", area_circulo(50), agora_iso(), agora_iso()),
    ]
    salvar_talhoes(talhoes)
    print("\n### DEMO: Talhões gravados")
    for t in talhoes:
        print(f"[{t.id}] {t.nome} | {t.cultura} | {t.area_ha:.4f} ha")
    # Insumos
    print("\n### DEMO: Insumos")
    calcular_insumo_area("Soja","Defensivo X",10,2.5)
    calcular_insumo_linhas("Milho","Adubo Y",100,50,0.02)
    # Exportação
    exportar_json(talhoes); exportar_csv(talhoes)
    print("\n### DEMO: concluído.")

# ------------------------------------------------------------
# Ponto de entrada
# ------------------------------------------------------------
if __name__ == "__main__":
    # MODO NORMAL (menu interativo):
    main()

    # Se sua IDE derrubar por inatividade, comente a linha acima e
    # descomente a linha abaixo para rodar a demonstração automática:
    # rodar_demo_rapida()