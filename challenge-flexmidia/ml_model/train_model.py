"""
EDUBOT - Modelo de Machine Learning
Sprint 2 - Challenge FlexMedia

Este script treina um modelo de classificação para prever
o tipo de interação (curto/longo) com base nos dados do totem.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score, 
    classification_report, 
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)
import joblib
import os
import sqlite3

# Caminhos
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "..", "database", "totem.db")
MODEL_PATH = os.path.join(SCRIPT_DIR, "model.pkl")
PLOTS_DIR = os.path.join(SCRIPT_DIR, "plots")

# Criar diretório de plots
os.makedirs(PLOTS_DIR, exist_ok=True)

# Configurações
np.random.seed(42)
plt.style.use('seaborn-v0_8-whitegrid')


def load_data() -> pd.DataFrame:
    """
    Carrega e prepara os dados do banco de dados.
    """
    print("📥 Carregando dados do banco de dados...")
    
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("""
        SELECT * FROM interacoes 
        WHERE ativacao = 1 
        AND tipo_interacao IN ('curto', 'longo')
    """, conn)
    conn.close()
    
    # Converter timestamp
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    print(f"✅ {len(df)} registros carregados para treinamento")
    return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria features para o modelo de ML.
    """
    print("\n🔧 Criando features...")
    
    df_features = df.copy()
    
    # Features temporais
    df_features['hora'] = df_features['timestamp'].dt.hour
    df_features['dia_semana'] = df_features['timestamp'].dt.dayofweek
    df_features['periodo_dia'] = pd.cut(
        df_features['hora'],
        bins=[0, 12, 18, 24],
        labels=['manha', 'tarde', 'noite'],
        include_lowest=True
    )
    
    # Feature de horário de pico (entre 10h e 14h e entre 18h e 20h)
    df_features['horario_pico'] = df_features['hora'].apply(
        lambda x: 1 if (10 <= x <= 14) or (18 <= x <= 20) else 0
    )
    
    # Fim de semana
    df_features['fim_semana'] = (df_features['dia_semana'] >= 5).astype(int)
    
    print(f"   ✅ Features criadas: hora, dia_semana, periodo_dia, horario_pico, fim_semana")
    
    return df_features


def prepare_data(df: pd.DataFrame):
    """
    Prepara os dados para treinamento.
    """
    print("\n📊 Preparando dados para treinamento...")
    
    # Definir features e target
    feature_columns = ['tempo_permanencia', 'hora', 'dia_semana', 'horario_pico', 'fim_semana']
    
    X = df[feature_columns].copy()
    y = df['tipo_interacao'].copy()
    
    # Codificar target
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    
    # Dividir dados
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )
    
    # Escalar features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"   - Treino: {len(X_train)} amostras")
    print(f"   - Teste: {len(X_test)} amostras")
    print(f"   - Features: {feature_columns}")
    print(f"   - Classes: {list(label_encoder.classes_)}")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, label_encoder, scaler, feature_columns


def train_models(X_train, X_test, y_train, y_test, label_encoder):
    """
    Treina e avalia diferentes modelos.
    """
    print("\n🤖 Treinando modelos de Machine Learning...")
    
    models = {
        'Decision Tree': DecisionTreeClassifier(
            max_depth=5,
            min_samples_split=5,
            random_state=42
        ),
        'Random Forest': RandomForestClassifier(
            n_estimators=100,
            max_depth=5,
            min_samples_split=5,
            random_state=42,
            n_jobs=-1
        )
    }
    
    results = {}
    
    for name, model in models.items():
        print(f"\n   📌 Treinando {name}...")
        
        # Treinar
        model.fit(X_train, y_train)
        
        # Prever
        y_pred = model.predict(X_test)
        
        # Métricas
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        # Validação cruzada
        cv_scores = cross_val_score(model, X_train, y_train, cv=5)
        
        results[name] = {
            'model': model,
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std(),
            'y_pred': y_pred
        }
        
        print(f"      Acurácia: {accuracy:.4f}")
        print(f"      Precisão: {precision:.4f}")
        print(f"      Recall: {recall:.4f}")
        print(f"      F1-Score: {f1:.4f}")
        print(f"      CV (5-fold): {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")
    
    return results


def plot_confusion_matrix(y_test, y_pred, labels, model_name):
    """
    Plota a matriz de confusão.
    """
    cm = confusion_matrix(y_test, y_pred)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
               xticklabels=labels, yticklabels=labels, ax=ax)
    
    ax.set_xlabel('Predição')
    ax.set_ylabel('Real')
    ax.set_title(f'EDUBOT - Matriz de Confusão\n{model_name}', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    
    filepath = os.path.join(PLOTS_DIR, f'confusion_matrix_{model_name.lower().replace(" ", "_")}.png')
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"   ✅ Matriz de confusão salva: {filepath}")


def plot_feature_importance(model, feature_names, model_name):
    """
    Plota a importância das features.
    """
    if hasattr(model, 'feature_importances_'):
        importance = model.feature_importances_
        
        # Ordenar por importância
        indices = np.argsort(importance)[::-1]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(feature_names)))
        
        bars = ax.barh(range(len(feature_names)), importance[indices], color=colors)
        ax.set_yticks(range(len(feature_names)))
        ax.set_yticklabels([feature_names[i] for i in indices])
        ax.invert_yaxis()
        ax.set_xlabel('Importância')
        ax.set_title(f'EDUBOT - Importância das Features\n{model_name}', fontsize=14, fontweight='bold')
        
        # Adicionar valores nas barras
        for bar, val in zip(bars, importance[indices]):
            ax.text(val + 0.01, bar.get_y() + bar.get_height()/2,
                   f'{val:.3f}', va='center', fontsize=10)
        
        plt.tight_layout()
        
        filepath = os.path.join(PLOTS_DIR, f'feature_importance_{model_name.lower().replace(" ", "_")}.png')
        plt.savefig(filepath, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"   ✅ Importância das features salva: {filepath}")


def plot_model_comparison(results):
    """
    Plota comparação entre os modelos.
    """
    metrics = ['accuracy', 'precision', 'recall', 'f1_score']
    model_names = list(results.keys())
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = np.arange(len(metrics))
    width = 0.35
    
    for i, (name, data) in enumerate(results.items()):
        values = [data[m] for m in metrics]
        offset = width * (i - 0.5)
        bars = ax.bar(x + offset, values, width, label=name, alpha=0.8)
        
        # Adicionar valores
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.3f}',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3), textcoords="offset points",
                       ha='center', va='bottom', fontsize=9)
    
    ax.set_xlabel('Métricas')
    ax.set_ylabel('Score')
    ax.set_title('EDUBOT - Comparação de Modelos de ML', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(['Acurácia', 'Precisão', 'Recall', 'F1-Score'])
    ax.legend()
    ax.set_ylim(0, 1.15)
    
    plt.tight_layout()
    
    filepath = os.path.join(PLOTS_DIR, 'model_comparison.png')
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"\n   ✅ Comparação de modelos salva: {filepath}")


def save_best_model(results, scaler, label_encoder, feature_columns):
    """
    Salva o melhor modelo.
    """
    print("\n💾 Salvando melhor modelo...")
    
    # Selecionar melhor modelo por F1-Score
    best_name = max(results, key=lambda x: results[x]['f1_score'])
    best_result = results[best_name]
    
    # Salvar modelo, scaler e encoder
    model_data = {
        'model': best_result['model'],
        'scaler': scaler,
        'label_encoder': label_encoder,
        'feature_columns': feature_columns,
        'metrics': {
            'accuracy': best_result['accuracy'],
            'precision': best_result['precision'],
            'recall': best_result['recall'],
            'f1_score': best_result['f1_score']
        },
        'model_name': best_name
    }
    
    joblib.dump(model_data, MODEL_PATH)
    
    print(f"   ✅ Modelo salvo: {MODEL_PATH}")
    print(f"   📌 Melhor modelo: {best_name}")
    print(f"   📊 F1-Score: {best_result['f1_score']:.4f}")
    
    return best_name, best_result


def predict_interaction(tempo_permanencia, hora, dia_semana):
    """
    Função utilitária para fazer predições com o modelo salvo.
    """
    # Carregar modelo
    model_data = joblib.load(MODEL_PATH)
    model = model_data['model']
    scaler = model_data['scaler']
    label_encoder = model_data['label_encoder']
    
    # Criar features
    horario_pico = 1 if (10 <= hora <= 14) or (18 <= hora <= 20) else 0
    fim_semana = 1 if dia_semana >= 5 else 0
    
    features = np.array([[tempo_permanencia, hora, dia_semana, horario_pico, fim_semana]])
    features_scaled = scaler.transform(features)
    
    # Predizer
    prediction = model.predict(features_scaled)
    prediction_label = label_encoder.inverse_transform(prediction)
    
    return prediction_label[0]


def main():
    """
    Função principal que executa o pipeline de ML.
    """
    print("=" * 60)
    print("EDUBOT - Treinamento de Modelo de Machine Learning")
    print("Sprint 2 - Challenge FlexMedia")
    print("=" * 60)
    
    # Carregar dados
    df = load_data()
    
    # Feature engineering
    df = feature_engineering(df)
    
    # Preparar dados
    X_train, X_test, y_train, y_test, label_encoder, scaler, feature_columns = prepare_data(df)
    
    # Treinar modelos
    results = train_models(X_train, X_test, y_train, y_test, label_encoder)
    
    # Gerar visualizações
    print("\n" + "=" * 60)
    print("GERANDO VISUALIZAÇÕES")
    print("=" * 60)
    
    for name, data in results.items():
        plot_confusion_matrix(y_test, data['y_pred'], label_encoder.classes_, name)
        plot_feature_importance(data['model'], feature_columns, name)
    
    plot_model_comparison(results)
    
    # Salvar melhor modelo
    best_name, best_result = save_best_model(results, scaler, label_encoder, feature_columns)
    
    # Relatório final
    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL")
    print("=" * 60)
    
    print(f"\n📊 Classification Report - {best_name}:")
    print(classification_report(y_test, best_result['y_pred'], 
                               target_names=label_encoder.classes_))
    
    print("\n✅ Treinamento concluído!")
    print(f"📁 Modelo salvo em: {MODEL_PATH}")
    print(f"📊 Gráficos salvos em: {PLOTS_DIR}")
    
    # Teste de predição
    print("\n" + "=" * 60)
    print("TESTE DE PREDIÇÃO")
    print("=" * 60)
    
    test_cases = [
        (30, 10, 2),   # 30s, 10h, quarta-feira
        (120, 14, 0),  # 120s, 14h, segunda-feira
        (45, 19, 5),   # 45s, 19h, sábado
    ]
    
    for tempo, hora, dia in test_cases:
        pred = predict_interaction(tempo, hora, dia)
        print(f"   Tempo: {tempo}s, Hora: {hora}h, Dia: {dia} → Predição: {pred}")
    
    return results


if __name__ == "__main__":
    results = main()
