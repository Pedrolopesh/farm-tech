import time
import json
import csv
from datetime import datetime

# --- PARÂMETROS DE IRRIGAÇÃO ---
PARAMETROS_CULTURA = {
    "Açaí": {"umidade_min": 45.0, "ph_min": 4.8, "ph_max": 6.2},
    "Soja": {"umidade_min": 35.0, "ph_min": 5.8, "ph_max": 7.0}
}

# --- FUNÇÃO DE LÓGICA DE DECISÃO ---


def decidir_irrigacao(dados_sensores: dict, cultura_atual: str) -> str:
    regras = PARAMETROS_CULTURA[cultura_atual]
    umidade = dados_sensores['umidade']
    ph = dados_sensores['ph']
    umidade_baixa = umidade < regras['umidade_min']
    ph_na_faixa = regras['ph_min'] <= ph <= regras['ph_max']
    if umidade_baixa and ph_na_faixa:
        return "LIGAR"
    else:
        return "DESLIGAR"

# --- PARTE E: FUNÇÃO DE LOGGING EM CSV ---


def registrar_dados(nome_arquivo: str, dados_sensores: dict, decisao: str):
    """
    Salva uma nova linha em um arquivo CSV com os dados atuais.
    """
    # Define o cabeçalho do CSV
    cabecalho = ['timestamp', 'n', 'p', 'k', 'ph', 'umidade', 'acao_bomba']

    # Cria uma nova linha de dados com o timestamp atual
    nova_linha = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'n': dados_sensores['n'],
        'p': dados_sensores['p'],
        'k': dados_sensores['k'],
        'ph': dados_sensores['ph'],
        'umidade': dados_sensores['umidade'],
        'acao_bomba': decisao
    }

    try:
        # 'a+' significa "append" (adicionar ao final), criando o arquivo se ele não existir
        with open(nome_arquivo, 'a+', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=cabecalho)

            # Escreve o cabeçalho apenas se o arquivo for novo (tamanho 0)
            f.seek(0)
            if f.tell() == 0:
                escritor.writeheader()

            # Escreve a nova linha de dados
            escritor.writerow(nova_linha)

    except IOError as e:
        print(f"Erro ao escrever no arquivo CSV: {e}")


# --- Dados Simulados ---
dados_simulados = [
    '{"n":0,"p":0,"k":0,"ph":6.5,"umidade":58.0}',
    '{"n":0,"p":0,"k":0,"ph":6.4,"umidade":45.1}',
    '{"n":0,"p":0,"k":0,"ph":6.1,"umidade":34.9}',
    '{"n":0,"p":0,"k":0,"ph":6.0,"umidade":34.8}',
    '{"n":0,"p":0,"k":0,"ph":7.8,"umidade":34.5}',
    '{"n":0,"p":0,"k":0,"ph":6.8,"umidade":60.2}',
]

# --- LOOP PRINCIPAL DA SIMULAÇÃO ---
CULTURA_MONITORADA = "Soja"
NOME_ARQUIVO_LOG = "python/historico_irrigacao.csv"
estado_bomba = "DESLIGAR"

print(f"--- Iniciando Simulação do Cérebro de Irrigação ---")
print(f"Monitorando a cultura: {CULTURA_MONITORADA}")
print(f"Registrando dados em: {NOME_ARQUIVO_LOG}")
print("(Pressione Ctrl+C para parar)")

try:
    while True:
        for json_string in dados_simulados:
            print(f"\nRecebido: {json_string}")

            try:
                dados_sensores = json.loads(json_string)
                decisao = decidir_irrigacao(dados_sensores, CULTURA_MONITORADA)

                print(
                    f"  -> Lógica aplicada: Umidade={dados_sensores['umidade']}%, pH={dados_sensores['ph']}")
                print(f"  ==> DECISÃO: {decisao}")

                # --- LÓGICA DE ENVIO DE COMANDO ---
                if decisao != estado_bomba:
                    print(
                        f"  ⚡️ AÇÃO: Enviando comando '{decisao}' para o ESP32.")
                    estado_bomba = decisao
                else:
                    print(f"  ... Nenhuma ação necessária.")

                # --- PARTE E: CHAMADA DA FUNÇÃO DE LOGGING ---
                registrar_dados(NOME_ARQUIVO_LOG, dados_sensores, estado_bomba)
                print(f"  -> Dados registrados em '{NOME_ARQUIVO_LOG}'.")

            except (json.JSONDecodeError, KeyError):
                print("  -> Erro: String JSON malformada ou dados faltando.")

            time.sleep(2)

except KeyboardInterrupt:
    print("\nSimulação interrompida pelo usuário.")

finally:
    print("Simulação finalizada.")
