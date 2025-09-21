# seeds.py
from datetime import date
from typing import List, Dict, Callable

def cadastrar_dados_teste(
    v_areas: List[Dict],
    next_id: Callable[[List[Dict]], int],
    calcula_area_retangulo: Callable[[float, float], Dict[str, float]],
    calcula_area_circulo: Callable[[float], Dict[str, float]],
    calc_manejo: Callable[[float, int, float], Dict[str, float]],
    CULTURA_ACAI: str,
    CULTURA_SOJA: str,
) -> None:
    """Insere 4 registros fictícios (2 Açaí + 2 Soja) dentro de v_areas."""
    hoje = date.today().isoformat()

    # 1) Açaí — retângulo
    largura, comprimento = 80.0, 200.0
    r_area = calcula_area_retangulo(largura, comprimento)
    taxa, num_ruas, comp_rua = 50.0, 10, 200.0
    r_m = calc_manejo(taxa, num_ruas, comp_rua)
    v_areas.append({
        "id": next_id(v_areas),
        "cultura": CULTURA_ACAI,
        "geometria": "retangulo",
        "largura_m": largura, "comprimento_m": comprimento, "raio_m": None,
        "area_m2": r_area["area_m2"], "area_ha": r_area["area_ha"],
        "created_at": hoje,
        "produto": "Fosfato", "taxa_ml_por_m": taxa, "num_ruas": num_ruas, "comprimento_m": comp_rua,
        "total_metros": r_m["total_metros"], "total_ml": r_m["total_ml"], "litros_totais": r_m["litros_totais"],
        "data_aplicacao": hoje, "equipamento": "Trator 01", "observacoes": "Aplicação inicial",
    })

    # 2) Açaí — retângulo
    largura, comprimento = 60.0, 150.0
    r_area = calcula_area_retangulo(largura, comprimento)
    taxa, num_ruas, comp_rua = 35.0, 8, 150.0
    r_m = calc_manejo(taxa, num_ruas, comp_rua)
    v_areas.append({
        "id": next_id(v_areas),
        "cultura": CULTURA_ACAI,
        "geometria": "retangulo",
        "largura_m": largura, "comprimento_m": comprimento, "raio_m": None,
        "area_m2": r_area["area_m2"], "area_ha": r_area["area_ha"],
        "created_at": hoje,
        "produto": "Herbicida X", "taxa_ml_por_m": taxa, "num_ruas": num_ruas, "comprimento_m": comp_rua,
        "total_metros": r_m["total_metros"], "total_ml": r_m["total_ml"], "litros_totais": r_m["litros_totais"],
        "data_aplicacao": hoje, "equipamento": "Trator 02", "observacoes": "Controle de daninhas",
    })

    # 3) Soja — círculo
    raio = 45.0
    r_area = calcula_area_circulo(raio)
    taxa, num_ruas, comp_rua = 60.0, 6, 100.0
    r_m = calc_manejo(taxa, num_ruas, comp_rua)
    v_areas.append({
        "id": next_id(v_areas),
        "cultura": CULTURA_SOJA,
        "geometria": "circulo",
        "largura_m": None, "comprimento_m": comp_rua, "raio_m": raio,
        "area_m2": r_area["area_m2"], "area_ha": r_area["area_ha"],
        "created_at": hoje,
        "produto": "Fosfato", "taxa_ml_por_m": taxa, "num_ruas": num_ruas,
        "total_metros": r_m["total_metros"], "total_ml": r_m["total_ml"], "litros_totais": r_m["litros_totais"],
        "data_aplicacao": hoje, "equipamento": "Pulverizador A", "observacoes": "Pré-plantio",
    })

    # 4) Soja — círculo
    raio = 30.0
    r_area = calcula_area_circulo(raio)
    taxa, num_ruas, comp_rua = 45.0, 7, 120.0
    r_m = calc_manejo(taxa, num_ruas, comp_rua)
    v_areas.append({
        "id": next_id(v_areas),
        "cultura": CULTURA_SOJA,
        "geometria": "circulo",
        "largura_m": None, "comprimento_m": comp_rua, "raio_m": raio,
        "area_m2": r_area["area_m2"], "area_ha": r_area["area_ha"],
        "created_at": hoje,
        "produto": "Herbicida Y", "taxa_ml_por_m": taxa, "num_ruas": num_ruas,
        "total_metros": r_m["total_metros"], "total_ml": r_m["total_ml"], "litros_totais": r_m["litros_totais"],
        "data_aplicacao": hoje, "equipamento": "Pulverizador B", "observacoes": "Pós-emergência",
    })

    print("✅ 4 registros de teste inseridos.")
