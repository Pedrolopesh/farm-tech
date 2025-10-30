from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from typing import Dict, List, Optional
import csv
import json
import pathlib

# =========================
# Catálogos e Constantes
# =========================
CULTURAS = ["Cana-de-açúcar", "Soja", "Açaí"]
CAT_RECEITA = [
    "Venda (grão/fruto)", "Subproduto", "Crédito rural", "Outras receitas"
]
CAT_DESPESA = [
    "Insumos", "Mão de obra", "Transporte", "Manutenção", "Combustível/Energia",
    "Arrendamento", "Impostos/Taxas", "Serviços/Consultoria", "Outras despesas"
]
METODOS_PAGAMENTO = ["Pix", "Dinheiro", "Cartão", "Boleto", "Transferência"]
UNIDADES = ["kg", "sc", "t", "L", "m³", "un"]

# =========================
# Base em memória
# =========================
transacoes: List[Dict] = []

def next_id() -> int:
    return (transacoes[-1]["id"] + 1) if transacoes else 1

# =========================
# Helpers de I/O e validação
# =========================
def _print_opcoes(opcoes: List[str]):
    for i, nome in enumerate(opcoes, start=1):
        print(f"[{i}] {nome}")

def read_choice(opcoes: List[str], prompt: str) -> str:
    while True:
        _print_opcoes(opcoes)
        raw = input(prompt).strip()
        try:
            idx = int(raw)
            if 1 <= idx <= len(opcoes):
                return opcoes[idx - 1]
        except ValueError:
            pass
        print(f"Opção inválida. Digite um número entre 1 e {len(opcoes)}.")

def read_yesno(prompt: str, default: bool = False) -> bool:
    suf = " [S/n]: " if default else " [s/N]: "
    while True:
        v = input(prompt + suf).strip().lower()
        if v == "" and default: return True
        if v == "" and not default: return False
        if v in ("s","sim","y","yes"): return True
        if v in ("n","nao","não","no"): return False
        print("Digite s para sim ou n para não.")

def read_nonempty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s: return s
        print("Valor obrigatório.")

def read_decimal(prompt: str, positivo: bool = True, casas_quant: bool = False) -> Decimal:
    while True:
        raw = input(prompt).strip()
        if raw == "":
            print("Valor obrigatório.")
            continue
        normalizado = raw.replace(".", "").replace(",", ".")
        try:
            v = Decimal(normalizado)
            if positivo and v <= 0:
                print("Valor deve ser maior que zero.")
                continue
            v = v.quantize(Decimal("0.000")) if casas_quant else v.quantize(Decimal("0.01"))
            return v
        except InvalidOperation:
            print("Valor inválido. Exemplos: 10, 99.90, 1.234,56")

def read_date(prompt: str, default_today: bool = True) -> date:
    while True:
        raw = input(prompt + (" (DD/MM/AAAA, Enter=hoje): " if default_today else " (DD/MM/AAAA): ")).strip()
        if raw == "" and default_today:
            return date.today()
        try:
            return datetime.strptime(raw, "%d/%m/%Y").date()
        except ValueError:
            print("Data inválida. Use DD/MM/AAAA.")

def read_opcional(prompt: str) -> Optional[str]:
    s = input(prompt + " (opcional): ").strip()
    return s if s else None

# =========================
# Prompts de domínio
# =========================
def prompt_tipo() -> str:
    return read_choice(["Receita", "Despesa"], "\nTipo de transação: ")

def prompt_cultura() -> str:
    print("\nVincular a qual cultura?")
    return read_choice(CULTURAS, "Escolha: ")

def prompt_categoria(tipo: str) -> str:
    print("\nCategoria:")
    return read_choice(CAT_RECEITA if tipo == "Receita" else CAT_DESPESA, "Escolha: ")

def prompt_unidade() -> str:
    print("\nUnidade de medida:")
    return read_choice(UNIDADES, "Escolha: ")

def prompt_metodo_pagamento() -> str:
    print("\nMétodo de pagamento:")
    return read_choice(METODOS_PAGAMENTO, "Escolha: ")

# =========================
# CRUD de Transações
# =========================
def criar_transacao() -> Dict:
    print("\n==============================")
    print("   Cadastro de Transação 💰   ")
    print("==============================")

    tipo = prompt_tipo()
    dmov = read_date("Data")
    cultura = prompt_cultura() if read_yesno("Deseja vincular a uma cultura específica?", True) else None
    categoria = prompt_categoria(tipo)
    descricao = read_nonempty("Descrição: ")

    usar_quant = read_yesno("Deseja informar quantidade/unidade?", True)
    if usar_quant:
        quantidade = read_decimal("Quantidade: ", positivo=True, casas_quant=True)
        unidade = prompt_unidade()
        preco_unit = read_decimal("Preço unitário (R$): ", positivo=True)
        total = (quantidade * preco_unit).quantize(Decimal("0.01"))
    else:
        quantidade = Decimal("1.000")
        unidade = "un"
        total = read_decimal("Total (R$): ", positivo=True)
        preco_unit = total

    metodo = prompt_metodo_pagamento()
    contraparte = read_opcional("Contraparte (cliente/fornecedor)")
    observacoes = read_opcional("Observações")

    valor_assinado = total if tipo == "Receita" else (total * Decimal("-1"))

    reg = {
        "id": next_id(),
        "tipo": tipo,
        "data": dmov.isoformat(),
        "cultura": cultura,                 # "Cana-de-açúcar" | "Soja" | "Açaí" | None
        "categoria": categoria,
        "descricao": descricao,
        "quantidade": str(quantidade),      # strings para evitar issues de Decimal
        "unidade": unidade,
        "preco_unitario": str(preco_unit),
        "total": str(total),
        "valor_assinado": str(valor_assinado),
        "metodo_pagamento": metodo,
        "contraparte": contraparte,
        "observacoes": observacoes,
        "created_at": date.today().isoformat(),
    }
    return reg

def cadastrar():
    reg = criar_transacao()
    transacoes.append(reg)
    print("✅ Transação cadastrada!")

def localizar_index_por_id(_id: int) -> Optional[int]:
    for i, t in enumerate(transacoes):
        if t["id"] == _id:
            return i
    return None

def listar(filtro_cultura: Optional[str] = None):
    print("\n=== Lista de Transações ===")
    if not transacoes:
        print("(vazio)")
        return
    for t in transacoes:
        if filtro_cultura and t.get("cultura") != filtro_cultura:
            continue
        print(f"ID {t['id']:03d} | {t['data']} | {t['tipo']} | {t.get('cultura') or '-'} | {t['categoria']} | {t['descricao']} | R$ {t['total']} | {t['metodo_pagamento']}")

def remover():
    if not transacoes:
        print("Não há transações para remover.")
        return
    try:
        _id = int(input("Informe o ID a remover: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    idx = localizar_index_por_id(_id)
    if idx is None:
        print("ID não encontrado.")
        return
    print("Selecionado:", transacoes[idx])
    if read_yesno("Confirmar remoção?", False):
        transacoes.pop(idx)
        print("🗑️ Removido com sucesso.")
    else:
        print("Remoção cancelada.")

def corrigir_transacao():
    """
    Correção campo-a-campo: o usuário escolhe qual campo editar.
    Mantém o mesmo ID e valida cada entrada.
    """
    if not transacoes:
        print("Não há transações para corrigir.")
        return
    try:
        _id = int(input("Informe o ID para corrigir: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    idx = localizar_index_por_id(_id)
    if idx is None:
        print("ID não encontrado.")
        return
    reg = transacoes[idx]
    print("\nTransação atual:")
    print(reg)

    campos_editaveis = [
        "data", "tipo", "cultura", "categoria", "descricao",
        "quantidade", "unidade", "preco_unitario", "total",
        "metodo_pagamento", "contraparte", "observacoes"
    ]
    print("\nQuais campos deseja editar?")
    _print_opcoes(campos_editaveis)
    print("[0] Cancelar")
    escolhas = input("Informe números separados por vírgula (ex.: 1,3,7): ").strip()
    if escolhas == "0" or escolhas == "":
        print("Correção cancelada.")
        return

    alvos = []
    for parte in escolhas.split(","):
        parte = parte.strip()
        if not parte.isdigit(): continue
        k = int(parte)
        if 1 <= k <= len(campos_editaveis):
            alvos.append(campos_editaveis[k-1])

    if not alvos:
        print("Nenhum campo válido selecionado.")
        return

    # Edição guiada com validação
    for campo in alvos:
        if campo == "data":
            reg["data"] = read_date("Nova data").isoformat()
        elif campo == "tipo":
            reg["tipo"] = prompt_tipo()
        elif campo == "cultura":
            reg["cultura"] = prompt_cultura() if read_yesno("Vincular cultura?", True) else None
        elif campo == "categoria":
            reg["categoria"] = prompt_categoria(reg["tipo"])
        elif campo == "descricao":
            reg["descricao"] = read_nonempty("Nova descrição: ")
        elif campo == "quantidade":
            q = read_decimal("Nova quantidade: ", positivo=True, casas_quant=True)
            reg["quantidade"] = str(q)
        elif campo == "unidade":
            reg["unidade"] = prompt_unidade()
        elif campo == "preco_unitario":
            pu = read_decimal("Novo preço unitário (R$): ", positivo=True)
            reg["preco_unitario"] = str(pu)
        elif campo == "total":
            tot = read_decimal("Novo total (R$): ", positivo=True)
            reg["total"] = str(tot)
        elif campo == "metodo_pagamento":
            reg["metodo_pagamento"] = prompt_metodo_pagamento()
        elif campo == "contraparte":
            reg["contraparte"] = read_opcional("Nova contraparte")
        elif campo == "observacoes":
            reg["observacoes"] = read_opcional("Novas observações")

    # Recalcula valor_assinado (coerência)
    total = Decimal(reg["total"])
    reg["valor_assinado"] = str(total if reg["tipo"] == "Receita" else (total * Decimal("-1")))

    transacoes[idx] = reg
    print("✅ Transação corrigida.")
    print(reg)

# =========================
# Exportação e Relatórios
# =========================
def exportar_csv(dirpath: str = "export"):
    p = pathlib.Path(dirpath)
    p.mkdir(parents=True, exist_ok=True)
    cols = [
        "id","data","tipo","cultura","categoria","descricao",
        "quantidade","unidade","preco_unitario","total",
        "valor_assinado","metodo_pagamento","contraparte","observacoes","created_at"
    ]
    with open(p / "transacoes.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for t in transacoes:
            w.writerow({k: t.get(k, "") for k in cols})
    print(f"💾 CSV exportado em {p/'transacoes.csv'}")

def exportar_json(path: str = "export/transacoes.json"):
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(transacoes, f, ensure_ascii=False, indent=2)
    print(f"💾 JSON exportado em {p}")

def resumo_por_cultura():
    """
    Inovação simples e útil: visão de margem por cultura (soma de receitas e despesas).
    """
    print("\n=== Resumo por Cultura ===")
    if not transacoes:
        print("(sem dados)")
        return

    acc = {c: {"receita": Decimal("0.00"), "despesa": Decimal("0.00"), "margem": Decimal("0.00")} for c in CULTURAS}
    acc["Sem vínculo"] = {"receita": Decimal("0.00"), "despesa": Decimal("0.00"), "margem": Decimal("0.00")}

    for t in transacoes:
        chave = t.get("cultura") or "Sem vínculo"
        val = Decimal(t["valor_assinado"])
        if val >= 0:
            acc[chave]["receita"] += val
        else:
            acc[chave]["despesa"] += val
        acc[chave]["margem"] = acc[chave]["receita"] + acc[chave]["despesa"]

    print("Cultura              | Receita (R$) | Despesa (R$) | Margem (R$)")
    print("---------------------+--------------+--------------+-------------")
    for cultura, d in acc.items():
        rec = f"{d['receita']:.2f}"
        des = f"{d['despesa']:.2f}"
        mar = f"{d['margem']:.2f}"
        print(f"{cultura:<21} | {rec:>12} | {des:>12} | {mar:>11}")

# =========================
# Seeds para testes (opcional)
# =========================
def seed_exemplo():
    # Receita Soja
    transacoes.append({
        "id": next_id(), "tipo": "Receita", "data": date.today().isoformat(),
        "cultura": "Soja", "categoria": "Venda (grão/fruto)", "descricao": "Venda 50 sc soja",
        "quantidade": "50.000", "unidade": "sc", "preco_unitario": "160.00", "total": "8000.00",
        "valor_assinado": "8000.00", "metodo_pagamento": "Pix",
        "contraparte": "Cooperativa X", "observacoes": None, "created_at": date.today().isoformat()
    })
    # Despesa Cana
    transacoes.append({
        "id": next_id(), "tipo": "Despesa", "data": date.today().isoformat(),
        "cultura": "Cana-de-açúcar", "categoria": "Insumos", "descricao": "Adubo NPK",
        "quantidade": "200.000", "unidade": "kg", "preco_unitario": "3.50", "total": "700.00",
        "valor_assinado": "-700.00", "metodo_pagamento": "Boleto",
        "contraparte": "Fornecedor Y", "observacoes": "Parcela 1/3", "created_at": date.today().isoformat()
    })
    # Despesa Açaí
    transacoes.append({
        "id": next_id(), "tipo": "Despesa", "data": date.today().isoformat(),
        "cultura": "Açaí", "categoria": "Manutenção", "descricao": "Reparo bomba d’água",
        "quantidade": "1.000", "unidade": "un", "preco_unitario": "450.00", "total": "450.00",
        "valor_assinado": "-450.00", "metodo_pagamento": "Dinheiro",
        "contraparte": "Oficina Z", "observacoes": None, "created_at": date.today().isoformat()
    })
    print("🔧 Seeds inseridos.")

# =========================
# Menu
# =========================
def menu():
    while True:
        print("\n=== Menu ===")
        print("[1] Cadastrar transação")
        print("[2] Listar transações")
        print("[3] Corrigir (editar) transação")
        print("[4] Remover transação")
        print("[5] Resumo por cultura")
        print("[6] Exportar CSV")
        print("[7] Exportar JSON")
        print("[8] Carregar seeds de exemplo")
        print("[0] Sair")
        op = input("Escolha: ").strip()
        if op == "1":
            cadastrar()
        elif op == "2":
            if read_yesno("Filtrar por cultura?", False):
                cultura = prompt_cultura()
                listar(cultura)
            else:
                listar()
        elif op == "3":
            corrigir_transacao()
        elif op == "4":
            remover()
        elif op == "5":
            resumo_por_cultura()
        elif op == "6":
            exportar_csv()
        elif op == "7":
            exportar_json()
        elif op == "8":
            seed_exemplo()
        elif op == "0":
            print("Até mais! 🌱")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
