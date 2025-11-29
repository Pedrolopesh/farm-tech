# 🎬 ROTEIRO SIMPLIFICADO - EDUBOT Sprint 2
## Vídeo de 5 minutos | Coleta de Dados e Análise

---

## ⏱️ CRONOGRAMA

| Tempo | Seção | Duração |
|-------|-------|---------|
| 0:00 - 0:25 | Introdução | 25s |
| 0:25 - 1:10 | Simulação de Sensores | 45s |
| 1:10 - 1:50 | Banco de Dados | 40s |
| 1:50 - 2:50 | Análise de Dados | 60s |
| 2:50 - 3:50 | Machine Learning | 60s |
| 3:50 - 4:45 | Dashboard | 55s |
| 4:45 - 5:00 | Encerramento | 15s |

---

## 🎬 CENA 1: INTRODUÇÃO (0:00 - 0:25)

**🎙️ FALA:**
> "Olá! Somos a equipe EDUBOT do Challenge FlexMedia da FIAP. Vamos demonstrar nosso pipeline de dados: simulação de sensores, banco de dados, análise estatística, Machine Learning e dashboard. Vamos lá!"

**📺 MOSTRAR:** Estrutura de pastas no VS Code

---

## 🎬 CENA 2: SIMULAÇÃO DE SENSORES (0:25 - 1:10)

**📁 ARQUIVO:** `sensors_simulation/simulated_sensors.py`

**🎙️ FALA:**
> "Começamos simulando os sensores do totem. Este script gera 200 registros realistas."

**📍 MOSTRAR NO CÓDIGO (linhas 80-95):**
```python
data.append({
    'timestamp': ts,
    'ativacao': ativacao,
    'tipo_interacao': tipo_interacao,
    'tempo_permanencia': tempo_permanencia,
    'sessao_id': sessao_id
})
```

> "Cada registro tem: timestamp, ativação, tipo de interação, tempo de permanência e ID de sessão."

**⌨️ EXECUTAR:**
```bash
python sensors_simulation/simulated_sensors.py
```

> "Pronto! 200 registros gerados com 96% de taxa de ativação."

**📺 MOSTRAR:** Saída do terminal + abrir `simulated_sensors.csv`

---

## 🎬 CENA 3: BANCO DE DADOS (1:10 - 1:50)

**📁 ARQUIVO:** `database/init_db.py`

**🎙️ FALA:**
> "Agora salvamos no SQLite. Veja o schema da tabela:"

**📍 MOSTRAR NO CÓDIGO (linhas 28-38):**
```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS interacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME NOT NULL,
        ativacao INTEGER NOT NULL CHECK(ativacao IN (0, 1)),
        tipo_interacao TEXT NOT NULL,
        tempo_permanencia INTEGER NOT NULL,
        sessao_id TEXT NOT NULL UNIQUE
    )
""")
```

> "Temos validações: ativação só aceita 0 ou 1, sessão é única."

**⌨️ EXECUTAR:**
```bash
python database/init_db.py
```

> "200 registros inseridos no banco SQLite."

---

## 🎬 CENA 4: ANÁLISE DE DADOS (1:50 - 2:50)

**📁 ARQUIVO:** `analysis/data_analysis.py`

**🎙️ FALA:**
> "Agora a análise. Primeiro, validação de qualidade:"

**📍 MOSTRAR NO CÓDIGO (linhas 55-68):**
```python
quality_report = {
    'total_registros': len(df),
    'duplicados': df.duplicated(subset=['sessao_id']).sum(),
    'valores_nulos': df.isnull().sum().to_dict(),
    'ativacao_valida': df['ativacao'].isin([0, 1]).all(),
}
```

> "Verificamos duplicados, nulos e valores válidos."

**🎙️ FALA:**
> "Depois, criamos features derivadas:"

**📍 MOSTRAR NO CÓDIGO (linhas 90-100):**
```python
df_clean['data'] = df_clean['timestamp'].dt.date
df_clean['hora'] = df_clean['timestamp'].dt.hour
df_clean['dia_semana'] = df_clean['timestamp'].dt.day_name()
```

**⌨️ EXECUTAR:**
```bash
python analysis/data_analysis.py
```

> "KPIs: 200 detecções, 96% ativação, tempo médio de 85 segundos."

**📺 MOSTRAR GRÁFICOS (abrir imagens):**
- `analysis/plots/interacoes_por_dia.png` → "Interações por dia"
- `analysis/plots/tipos_interacao.png` → "62% curtas, 38% longas"
- `analysis/plots/heatmap_uso.png` → "Padrões de uso por dia e hora"

---

## 🎬 CENA 5: MACHINE LEARNING (2:50 - 3:50)

**📁 ARQUIVO:** `ml_model/train_model.py`

**🎙️ FALA:**
> "Objetivo: classificar se a interação será curta ou longa."

**📍 MOSTRAR NO CÓDIGO (linhas 95-100):**
```python
feature_columns = ['tempo_permanencia', 'hora', 'dia_semana', 'horario_pico', 'fim_semana']
X = df[feature_columns].copy()
y = df['tipo_interacao'].copy()
```

> "Usamos 5 features: tempo, hora, dia, horário de pico e fim de semana."

**📍 MOSTRAR NO CÓDIGO (linhas 130-145):**
```python
models = {
    'Decision Tree': DecisionTreeClassifier(max_depth=5),
    'Random Forest': RandomForestClassifier(n_estimators=100)
}
```

> "Treinamos Decision Tree e Random Forest."

**⌨️ EXECUTAR:**
```bash
python ml_model/train_model.py
```

> "100% de acurácia! O tempo de permanência é a feature mais importante."

**📺 MOSTRAR GRÁFICOS:**
- `ml_model/plots/confusion_matrix_decision_tree.png` → "Zero erros"
- `ml_model/plots/feature_importance_random_forest.png` → "Tempo de permanência domina"

**📍 MOSTRAR PREDIÇÃO NO TERMINAL:**
> "Teste: 30s às 10h = CURTO. 120s às 14h = LONGO."

---

## 🎬 CENA 6: DASHBOARD (3:50 - 4:45)

**📁 ARQUIVO:** `dashboard/app.py`

**⌨️ EXECUTAR:**
```bash
streamlit run dashboard/app.py
```

**📺 NO NAVEGADOR (localhost:8501):**

**🎙️ FALA:**
> "Dashboard Streamlit com KPIs em tempo real."

**📍 MOSTRAR:**
1. **KPIs no topo** → "Total de detecções, ativações, tempo médio"
2. **Aba Gráficos** → "Timeline interativa e pizza de tipos"
3. **Aba Heatmap** → "Padrões de uso"
4. **Sidebar** → "Filtros por período e tipo"
5. **Aba ML** → "Teste de predição ao vivo"

**🎙️ DEMONSTRAR PREDIÇÃO:**
> "Vou testar: 120 segundos, 14h, quarta-feira... Resultado: LONGO!"

---

## 🎬 CENA 7: ENCERRAMENTO (4:45 - 5:00)

**🎙️ FALA:**
> "Resumo da Sprint 2: simulamos 200 registros, salvamos no SQLite, analisamos com 5 gráficos, treinamos modelo com 100% de acurácia e criamos dashboard interativo.
> 
> Obrigado! Equipe EDUBOT, turma R, FIAP."

---

## 📋 CHECKLIST RÁPIDO

```bash
# Antes de gravar, execute tudo uma vez:
cd challenge-flexmidia
source venv/bin/activate
rm -f sensors_simulation/*.csv database/*.db  # Limpar para demo
python sensors_simulation/simulated_sensors.py
python database/init_db.py
python analysis/data_analysis.py
python ml_model/train_model.py
streamlit run dashboard/app.py
```

## 📍 LINHAS IMPORTANTES POR ARQUIVO

| Arquivo | O que mostrar | Linhas |
|---------|---------------|--------|
| `simulated_sensors.py` | Estrutura dos dados | 80-95 |
| `init_db.py` | Schema da tabela | 28-38 |
| `data_analysis.py` | Validação de qualidade | 55-68 |
| `data_analysis.py` | Features derivadas | 90-100 |
| `train_model.py` | Features do ML | 95-100 |
| `train_model.py` | Modelos treinados | 130-145 |

---

**🎬 Boa gravação!**
