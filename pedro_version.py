''''
- Culturas: Açai (área retangular) e Soja (área circular).
- Manejo: cálculo por mL por metro × nº de ruas × metragem ⇒ litros totais
- Dados em vetores (listas)
- Menu com entrada/saída/atualização/deleção/sair
- Uso de loops e decisões
- Exportação para CSV (para uso no R)
'''
import csv
import math
import pathlib
from datetime import date
from typing import List, Dict, Optional


# =========================
# "Banco de dados" em memória (vetores/listas)
# =========================
def next_id(v: List[Dict]) -> int:
    return (v[-1]["id"] + 1) if v else 1

CULTURA_ACAI = "Açaí"
CULTURA_SOJA = "Soja"

v_areas: List[Dict] = []
v_applications: List[Dict] = []


# =========================
# Helpers de entrada (funções para auxiliar na leitura de dados)
# =========================
def read_float(typed_prompt: str)-> float:
    while True:
        txt = input(typed_prompt).strip().replace(",", ".")
        try:
            return float(txt)
        except ValueError:
            print("Valor inválido. Tente novamente (use números).")

def read_int(prompt: str) -> int:
    while True:
        txt = input(prompt).strip()
        try:
            return int(txt)
        except ValueError:
            print("Inteiro inválido. Tente novamente.")

# =========================
# Funções puras de cálculo
# =========================
def calcula_area_retangulo(largura_m: float, comprimento_m: float) -> Dict[str, float]:
    area_m2 = largura_m * comprimento_m
    return {"area_m2": round(area_m2, 2), "area_ha": round(area_m2 / 10_000, 4)}

def calcula_area_circulo(raio: float) -> Dict[str, float]:
    area_m2_circulo = math.pi * (raio**2)
    return {"area_m2": round(area_m2_circulo, 2), "area_ha": round(area_m2_circulo / 10_000, 4)}

def calc_manejo(taxa_ml_por_m: float, num_ruas: int, comprimento_m: float) -> Dict[str, float]:
    total_metros = num_ruas * comprimento_m
    total_ml = taxa_ml_por_m * total_metros
    litros_totais = total_ml / 1000.0
    return {
        "total_metros": round(total_metros, 2),
        "total_ml": round(total_ml, 2),
        "litros_totais": round(litros_totais, 3),
    }


# =========================
# Camada interativa (lê input, usa funções puras)
# =========================
def cadastra_areas():
    print("\n== Cadastro de Área ==")
    print("[1] Açaí (retângulo)  |  [2] Soja (círculo)")
    user_option = input("Escolha a cultura (1/2): ").strip()

    if user_option == "1":
        cultura = CULTURA_ACAI
        largura = read_float("Largura (m): ")
        comprimento = read_float("Comprimento (m): ")
        resultado_total = calcula_area_retangulo(largura, comprimento)
        registro_total = {
            "id": next_id(v_areas),
            "cultura": cultura,
            "geometria": "retangulo",
            "largura_m": largura,
            "comprimento_m": comprimento,
            "raio_m": None,
            "area_m2": resultado_total["area_m2"],
            "area_ha": resultado_total["area_ha"],
            "created_at": date.today().isoformat(),
        }
        v_areas.append(registro_total)

    elif user_option == "2":
        cultura = CULTURA_SOJA
        raio = read_float("Raio (m): ")
        resultado_total = calcula_area_circulo(raio)
        registro_total = {
            "id": next_id(v_applications),
            "cultura": cultura,
            "geometria": "circulo",
            "largura_m": None,
            "comprimento_m": None,
            "raio_m": raio,
            "area_m2": resultado_total["area_m2"],
            "area_ha": resultado_total["area_ha"],
            "created_at": date.today().isoformat(),
        }
        v_areas.append(registro_total)
    else:
        print("Opção inválida. Não existe essa opção para cadastro de areas.")
        return

    print("✅ Área cadastrada!")
    print(v_areas[-1])


# =========================
# Cadastro do manejo de insumos
# =========================
def cadastra_manejo():
    print("\n== Cadastro de Manejo de Insumos ==")
    print("Selecione uma das opções: [1] Açaí  |  [2] Soja")
    user_option = input("Cultura (1/2): ").strip()
    cultura = "Açaí" if user_option == "1" else "Soja" if user_option == "2" else None
    if not cultura:
        print("Opção inválida.")
        return


    produto = input("Produto (ex.: Fosfato): ").strip() or "Produto"
    taxa = read_float("Taxa (mL por metro): ")
    ruas = read_int("Número de ruas: ")
    comp = read_float("Comprimento de cada rua (m): ")

    resultado_calc_manejo = calc_manejo(taxa, ruas, comp)
    registro_total = {
        "id": next_id(v_areas),
        "cultura": cultura,
        "produto": produto,
        "taxa_ml_por_m": taxa,
        "num_ruas": ruas,
        "comprimento_m": comp,
        "total_metros": resultado_calc_manejo["total_metros"],
        "total_ml": resultado_calc_manejo["total_ml"],
        "litros_totais": resultado_calc_manejo["litros_totais"],
        "data_aplicacao": date.today().isoformat(),
        "equipamento": "",
        "observacoes": "",
    }
    v_applications.append(registro_total)
    print("✅ Manejo registrado!")
    print(v_applications[-1])

def listar():
    print("\n== Áreas ==")
    if not v_areas:
        print("(vazio)")
    else:
        for f in v_areas:
            print(f)

    print("\n== Manejos ==")
    if not v_applications:
        print("(vazio)")
    else:
        for a in v_applications:
            print(a)

def exportar_csv(dirpath: str = "python"):
    p = pathlib.Path(dirpath)
    p.mkdir(parents=True, exist_ok=True)

    cols_fields = [
        "id","cultura","geometria","largura_m","comprimento_m","raio_m",
        "area_m2","area_ha","created_at"
    ]
    with open(p / "fields.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols_fields)
        w.writeheader()
        for r in v_areas:
            w.writerow(r)

    cols_apps = [
        "id","cultura","produto","taxa_ml_por_m","num_ruas","comprimento_m",
        "total_metros","total_ml","litros_totais","data_aplicacao","equipamento","observacoes"
    ]
    with open(p / "applications.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols_apps)
        w.writeheader()
        for r in v_applications:
            w.writerow(r)

    print(f"💾 CSVs exportados em {p}/")

def menu_inicial():
    while True:
        print("\n=== Menu ===")
        print("[1] Cadastrar área")
        print("[2] Cadastrar manejo")
        print("[3] Listar")
        print("[4] Exportar CSV")
        print("[0] Sair")
        user_option = input("Escolha uma das opções: ")
        if user_option == "1":
            cadastra_areas()
        elif user_option == "2":
            cadastra_manejo()
        elif user_option == "3":
            listar()
        elif user_option == "4":
            exportar_csv()
        elif user_option == "0":
            print("Até mais! 🌱")
            break
        else:
            print("Opção inválida. Não existe essa opção no menu")

if __name__ == "__main__":
    menu_inicial()