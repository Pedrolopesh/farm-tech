''''
- Culturas: Açai (área retangular) e Soja (área circular).
- Manejo: cálculo por mL por metro × nº de ruas × metragem ⇒ litros totais
- Dados em vetores (listas)
- Menu com entrada/saída/atualização/deleção/sair
- Uso de loops e decisões
- Exportação para CSV (para uso no R)
'''
import math
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
v_aplications: List[Dict] = []

def calcula_area_retangulo(largura_m: float, comprimento_m: float) -> Dict[str, float]:
    area_m2 = largura_m * comprimento_m
    return {"area_m2": round(area_m2, 2), "area_ha": round(area_m2 / 1000, 4)}

def calcula_area_circulo(raio: float) -> Dict[str, float]:
    area_m2_circulo = math.pi * (raio**2)
    return {"area_m2_circulo": round(area_m2_circulo, 2), "area_ha": round(area_m2_circulo / 1000, 4)}

def read_float(typed_prompt: str)-> float:
    while True:
        txt = input(typed_prompt).strip().replace(",", ".")
        try:
            return float(txt)
        except ValueError:
            print("Valor inválido. Tente novamente (use números).")



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
    else:
        print("Opção inválida.")
        return

    print("✅ Área cadastrada!")
    print(v_areas[-1])

def menu_inicial():
    while True:
        print("\n=== Menu ===")
        print("[1] Cadastrar área")
        print("[2] Cadastrar manejo")
        print("[3] Listar")
        print("[4] Exportar CSV")
        print("[0] Sair")
        user_option = input("Escolha uma das opções: ")
        if user_option == "1": cadastra_areas();
        elif user_option == "0":
            print("Até mais! 🌱")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu_inicial()