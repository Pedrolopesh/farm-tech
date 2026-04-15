import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

def train_sprint4_model():
    # 1. Carregamento dos dados do banco atualizado
    if not os.path.exists('database/totem.db'):
        print("❌ Erro: Banco de dados não encontrado. Rode o init_db.py primeiro.")
        return

    conn = sqlite3.connect('database/totem.db')
    df = pd.read_sql('SELECT * FROM interacoes', conn)
    conn.close()

    print(f"📊 Iniciando treinamento com {len(df)} registros...")

    # 2. Pré-processamento (Transformando Categorias em Números)
    # Mapeamos os novos dados de Visão e Perfil para que o modelo entenda
    df['perfil_n'] = df['perfil_usuario'].map({'Estudante': 0, 'Professor': 1, 'Visitante': 2})
    df['visao_n'] = df['humor_estimado'].map({'Focado': 0, 'Distraído': 1, 'Ausente': 2})

    # 3. Definição de Features (X) e Target (y)
    # AQUI ESTÁ A CORREÇÃO DO DATA LEAKAGE: 
    # Removemos 'tempo_permanencia_seg' das Features. 
    # O modelo agora usa apenas o COMPORTAMENTO para prever o RESULTADO.
    X = df[['toques_por_minuto', 'perfil_n', 'visao_n']]
    y = df['tipo_interacao']

    # 4. Divisão Treino e Teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 5. Treinamento do Modelo (Random Forest)
    # Mantivemos o Random Forest por ser robusto e lidar bem com variáveis categóricas
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 6. Avaliação Realista
    y_pred = model.predict(X_test)
    
    print("\n✅ Relatório de Performance (Sprint 4):")
    # A acurácia aqui será menor que 100%, o que prova a evolução do projeto
    print(classification_report(y_test, y_pred))

    # 7. Salvando o Modelo e a estrutura
    if not os.path.exists('ml_model'):
        os.makedirs('ml_model')
        
    joblib.dump(model, 'ml_model/modelo_edubot_v4.pkl')
    print("🚀 Modelo 'modelo_edubot_v4.pkl' salvo com sucesso!")

if __name__ == "__main__":
    train_sprint4_model()