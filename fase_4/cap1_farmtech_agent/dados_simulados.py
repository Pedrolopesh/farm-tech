import pandas as pd
import numpy as np

# Configuração da semente
np.random.seed(42)

# --- GERAÇÃO DA CULTURA: SOJA (500 Amostras) ---
n_soja = 500
# Soja não gosta de encharcamento extremo
umidade_soja = np.random.uniform(low=30, high=80, size=n_soja)
ph_soja = np.random.uniform(low=5.0, high=8.0, size=n_soja)
temp_soja = np.random.uniform(low=20, high=35, size=n_soja)
nutrientes_soja = np.random.uniform(low=3, high=9, size=n_soja)

# Fórmula de Rendimento da Soja (Ideal: Umidade 60, pH 6.5)
rend_soja = (
    (12 * nutrientes_soja) +
    (100 - abs(umidade_soja - 60) * 1.5) +  # Penaliza longe de 60%
    (100 - abs(ph_soja - 6.5) * 20) +       # Penaliza longe de pH 6.5
    (50 - abs(temp_soja - 25))
) / 10

# Cria dataframe da Soja
df_soja = pd.DataFrame({
    'Cultura': 'Soja',
    'Umidade_Solo': umidade_soja,
    'pH_Solo': ph_soja,
    'Temperatura': temp_soja,
    'Nivel_Nutrientes': nutrientes_soja,
    'Rendimento_Colheita': rend_soja
})

# --- GERAÇÃO DA CULTURA: AÇAÍ (500 Amostras) ---
n_acai = 500
# Açaí gosta de mais água (região amazônica)
umidade_acai = np.random.uniform(low=50, high=95, size=n_acai)
ph_acai = np.random.uniform(low=4.5, high=7.5, size=n_acai)
temp_acai = np.random.uniform(low=22, high=38, size=n_acai)  # Gosta de calor
nutrientes_acai = np.random.uniform(low=3, high=9, size=n_acai)

# Fórmula de Rendimento do Açaí (Ideal: Umidade 85, pH 5.8)
rend_acai = (
    (12 * nutrientes_acai) +
    # Penaliza longe de 85% (tolera mais água)
    (100 - abs(umidade_acai - 85) * 1.2) +
    (100 - abs(ph_acai - 5.8) * 15) +       # Penaliza longe de pH 5.8
    (50 - abs(temp_acai - 28))
) / 10

# Cria dataframe do Açaí
df_acai = pd.DataFrame({
    'Cultura': 'Acai',  # Evitar acentos no CSV ajuda a evitar bugs de encoding depois
    'Umidade_Solo': umidade_acai,
    'pH_Solo': ph_acai,
    'Temperatura': temp_acai,
    'Nivel_Nutrientes': nutrientes_acai,
    'Rendimento_Colheita': rend_acai
})

# --- JUNTAR TUDO ---
df_final = pd.concat([df_soja, df_acai])

# Embaralhar os dados (para não ficar tudo Soja primeiro, depois Açaí)
df_final = df_final.sample(frac=1).reset_index(drop=True)

# Adicionar ruído e tratar negativos
ruido = np.random.normal(0, 0.5, len(df_final))
df_final['Rendimento_Colheita'] = df_final['Rendimento_Colheita'] + ruido
df_final['Rendimento_Colheita'] = np.maximum(
    df_final['Rendimento_Colheita'], 0)

# Salvar
print("Amostra dos dados gerados (com Soja e Açaí):")
print(df_final.head(10))  # Mostra 10 linhas para ver se misturou

df_final.to_csv('dados_agricolas_farmtech.csv', index=False)
print("\nArquivo 'dados_agricolas_farmtech.csv' atualizado com sucesso!")
