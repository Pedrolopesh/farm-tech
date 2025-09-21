''''
- Culturas: Açai (área retangular) e Soja (área circular).
- Manejo: cálculo por mL por metro × nº de ruas × metragem ⇒ litros totais
- Dados em vetores (listas)
- Menu com entrada/saída/atualização/deleção/sair
- Uso de loops e decisões
- Exportação para CSV (para uso no local-tests)
'''
import csv
import math
import pathlib
from datetime import date
from typing import List, Dict, Optional
from seeds import cadastrar_dados_teste


# =========================
# "Banco de dados" em memória (vetores/listas)
# =========================
def next_id(v: List[Dict]) -> int:
    print(v)
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

def prompt_inline_item() -> Dict:
    print("\n== Cadastro de Talhão + Manejo ==")
    print("Selecione uma das opções: [1] Açaí  |  [2] Soja")
    user_option = input("Cultura (1/2): ").strip()

    if user_option == "1":
        cultura = CULTURA_ACAI
        largura = read_float("Largura (m): ")
        comprimento = read_float("Comprimento (m): ")
        resultado_total = calcula_area_retangulo(largura, comprimento)
        produto = input("Produto (ex.: Fosfato): ").strip() or " "
        taxa = read_float("Taxa (mL por metro): ")
        ruas = read_int("Número de ruas: ")

        resultado_calc_manejo = calc_manejo(taxa, ruas, comprimento)
        return {
            # id será definido FORA (no criar ou atualizar)
            "cultura": cultura,
            "geometria": "retangulo",
            "largura_m": largura,
            "comprimento_m": comprimento,
            "raio_m": None,
            "area_m2": resultado_total["area_m2"],
            "area_ha": resultado_total["area_ha"],        # (bom ter)
            "created_at": date.today().isoformat(),
            "produto": produto,
            "taxa_ml_por_m": taxa,
            "num_ruas": ruas,
            "comprimento_m": comprimento,                 # manter explícito
            "total_metros": resultado_calc_manejo["total_metros"],
            "total_ml": resultado_calc_manejo["total_ml"],
            "litros_totais": resultado_calc_manejo["litros_totais"],
            "data_aplicacao": date.today().isoformat(),
            "equipamento": "",
            "observacoes": "",
        }

    elif user_option == "2":
        cultura = CULTURA_SOJA
        raio = read_float("Raio (m): ")
        resultado_total = calcula_area_circulo(raio)
        produto = input("Produto (ex.: Fosfato): ").strip() or " "
        taxa = read_float("Taxa (mL por metro): ")
        ruas = read_int("Número de ruas: ")
        comprimento = read_float("Comprimento de cada rua (m): ")  # melhor pedir explicitamente

        resultado_calc_manejo = calc_manejo(taxa, ruas, comprimento)
        return {
            "cultura": cultura,
            "geometria": "circulo",
            "largura_m": None,
            "comprimento_m": comprimento,                 # comprimento do manejo
            "raio_m": raio,
            "area_m2": resultado_total["area_m2"],
            "area_ha": resultado_total["area_ha"],
            "created_at": date.today().isoformat(),
            "produto": produto,
            "taxa_ml_por_m": taxa,
            "num_ruas": ruas,
            "total_metros": resultado_calc_manejo["total_metros"],
            "total_ml": resultado_calc_manejo["total_ml"],
            "litros_totais": resultado_calc_manejo["litros_totais"],
            "data_aplicacao": date.today().isoformat(),
            "equipamento": "",
            "observacoes": "",
        }
    else:
        print("Opção inválida.")
        return {}


def cadastra_areas_manejos():
    print("\n== Cadastro de Manejo de Insumos ==")
    print("Selecione uma das opções: [1] Açaí  |  [2] Soja")
    user_option = input("Cultura (1/2): ").strip()

    if user_option == "1":
        registro_total = prompt_inline_item()
        v_areas.append(registro_total)

    elif user_option == "2":
        registro_total = prompt_inline_item()
        v_areas.append(registro_total)

    else:
        print("Opção inválida. Não existe essa opção para cadastro de areas.")
        return

    print("✅ Área cadastrada!")
    print(v_areas[-1])

def localizar_index_por_id(lista: List[Dict], _id: int) -> Optional[int]:
    for i, r in enumerate(lista):
        if r.get("id") == _id:
            return i
    return None

def remover_item():
    if not v_areas:
        print("Não há registros para remover.")
        return

    print("\n== Remover item ==")
    try:
        _id = read_int("Informe o ID do talhão a remover: ")
    except Exception:
        print("ID inválido.")
        return

    idx = localizar_index_por_id(v_areas, _id)
    if idx is None:
        print("ID não encontrado.")
        return

    print("Registro selecionado:")
    print(v_areas[idx])

    confirma = input("Tem certeza que deseja remover? (s/N): ").strip().lower()
    if confirma != "s":
        print("Remoção cancelada.")
        return

    removido = v_areas.pop(idx)
    print("🗑️  Removido com sucesso:")
    print(removido)

def atualizar_por_recadastro():
    if not v_areas:
        print("Não há registros para atualizar.")
        return

    print("\n== Atualizar (apagar e recadastrar) ==")
    _id = read_int("Informe o ID: ")
    idx = localizar_index_por_id(v_areas, _id)
    if idx is None:
        print("ID não encontrado.")
        return

    antigo = v_areas.pop(idx)                    # remove o antigo
    print("↩️ Agora recadastre o item (os dados antigos foram removidos).")
    novo = prompt_inline_item()                  # recria via prompts
    if not novo:
        print("Cancelado. Restaurando item antigo.")
        v_areas.insert(idx, antigo)              # volta o antigo se cancelou
        return

    novo["id"] = _id                             # preserva o mesmo ID
    v_areas.insert(idx, novo)                    # volta no MESMO índice
    print("✅ Item atualizado!")
    print(v_areas[idx])


def listar():
    print("\n== Áreas ==")
    if not v_areas:
        print("(vazio)")
    else:
        for f in v_areas:
            print(f)

    # print("\n== Manejos ==")
    # if not v_applications:
    #     print("(vazio)")
    # else:
    #     for a in v_applications:
    #         print(a)

def exportar_csv(dirpath: str = "python"):
    p = pathlib.Path(dirpath)
    p.mkdir(parents=True, exist_ok=True)

    # --- ÁREAS (fields.csv) ---
    cols_fields = [
        "id","cultura","geometria","largura_m","comprimento_m","raio_m",
        "area_m2","area_ha","created_at"
    ]
    with open(p / "fields.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols_fields)
        w.writeheader()
        for r in v_areas:
            w.writerow({k: r.get(k) for k in cols_fields})  # <-- pega só as colunas declaradas

    # --- MANEJOS (applications.csv) ---
    # Vamos "achatar" os dados de manejo a partir do próprio v_areas,
    # assumindo 1 manejo por talhão no seu fluxo atual.
    cols_apps = [
        "id","talhao_id","cultura","produto","taxa_ml_por_m","num_ruas","comprimento_m",
        "total_metros","total_ml","litros_totais","data_aplicacao","equipamento","observacoes"
    ]
    with open(p / "applications.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols_apps)
        w.writeheader()
        for t in v_areas:
            # Se houver manejo (produto preenchido), exporta uma linha
            if t.get("produto"):
                row = {
                    "id": 1,  # se quiser vários manejos por talhão no futuro, incremente aqui
                    "talhao_id": t["id"],
                    "cultura": t["cultura"],
                    "produto": t.get("produto", ""),
                    "taxa_ml_por_m": t.get("taxa_ml_por_m", ""),
                    "num_ruas": t.get("num_ruas", ""),
                    "comprimento_m": t.get("comprimento_m", ""),
                    "total_metros": t.get("total_metros", ""),
                    "total_ml": t.get("total_ml", ""),
                    "litros_totais": t.get("litros_totais", ""),
                    "data_aplicacao": t.get("data_aplicacao", ""),
                    "equipamento": t.get("equipamento", ""),
                    "observacoes": t.get("observacoes", ""),
                }
                w.writerow(row)

    print(f"💾 CSVs exportados em {p}/")


def menu_inicial():
    while True:
        print("\n=== Menu ===")
        print("[1] Cadastrar área e manejo")
        print("[2] Listar")
        print("[3] Alterar item cadastrado")
        print("[4] Remover item cadastrado")
        print("[5] Exportar CSV")
        print("[9] Cadastrar dados teste")
        print("[0] Sair")
        user_option = input("Escolha uma das opções: ")
        if user_option == "1":
            cadastra_areas_manejos()
        elif user_option == "2":
            listar()
        elif user_option == "3":
            atualizar_por_recadastro()
        elif user_option == "4":
            remover_item()
        elif user_option == "5":
            exportar_csv()
        elif user_option == "9":
            cadastrar_dados_teste(
                v_areas=v_areas,
                next_id=next_id,
                calcula_area_retangulo=calcula_area_retangulo,
                calcula_area_circulo=calcula_area_circulo,
                calc_manejo=calc_manejo,
                CULTURA_ACAI=CULTURA_ACAI,
                CULTURA_SOJA=CULTURA_SOJA,
            )
        elif user_option == "0":
            print("Até mais! 🌱")
            break
        else:
            print("Opção inválida. Não existe essa opção no menu")

if __name__ == "__main__":
    menu_inicial()