# EDUBOT - Sprint 3: Inteligência Preditiva e Engajamento Avançado
### Challenge FlexMedia - Sprint 3
**Tecnólogo em Inteligência Artificial - FIAP** *"Modelagem de dados complexos e predição de engajamento em tempo real"*

**Repositório:** [https://github.com/Pedrolopesh/farm-tech](https://github.com/Pedrolopesh/farm-tech)

---

## 📋 Índice
1. [Visão Geral da Sprint 3](#-visão-geral-da-sprint-3)
2. [Novidades desta Versão](#-novidades-desta-versão)
3. [Estrutura do Projeto](#-estrutura-do-projeto)
4. [Guia de Execução](#-guia-de-execução)
5. [Machine Learning Avançado](#-machine-learning-avançado)
6. [Dashboard de Monitoramento](#-dashboard-de-monitoramento)
7. [Resultados e Métricas](#-resultados-e-métricas)
8. [Equipe](#-equipe)

---

## 🎯 Visão Geral da Sprint 3
A Sprint 3 do EDUBOT marca a evolução do sistema de monitoramento para uma plataforma de **Inteligência de Dados**. Expandimos a base de dados para 1.500 registros e introduzimos métricas de comportamento humano (frequência de toques) para classificar o nível de interesse do produtor rural.

### Objetivos Alcançados
* ✅ **Big Data Simulação:** Expansão para 1.500 registros cobrindo o período de 2025 a 2026.
* ✅ **Novas Variáveis:** Inclusão de `toques_por_minuto` e `velocidade_toques` (alta/baixa).
* ✅ **ML de Alta Precisão:** Implementação do Random Forest com 100% de acurácia nos padrões de treino.
* ✅ **Dashboard Interativo:** Interface Streamlit com filtros de data, gráficos de tendência e simulador de IA.
* ✅ **Persistência Evoluída:** Reestruturação do banco SQLite para suportar as novas colunas de engajamento.

---

## ✨ Novidades desta Versão
Diferente da Sprint 2, agora monitoramos não apenas o "tempo", mas a **intensidade** da interação:
* **Interação Média:** Nova categoria adicionada para maior granularidade.
* **Análise de Toques:** O sistema agora diferencia um usuário curioso (muitos toques) de um usuário passivo.
* **Filtros Temporais:** O Dashboard permite selecionar períodos específicos no calendário.

---

## 📁 Estrutura do Projeto
```text
challenge-flexmidia/
├── sensors_simulation/
│   ├── simulated_sensors.py      # Script v3.0 (1500 registros + métricas de toque)
│   └── edubot_sensor_data.csv    # Novo Dataset expandido
├── database/
│   ├── init_db.py                # Script de recriação do banco com novas colunas
│   └── totem.db                  # SQLite atualizado
├── ml_model/
│   ├── train_model.py            # Treinamento do Random Forest
│   └── modelo_edubot.pkl         # Modelo serializado de alta performance
├── analysis/
│   ├── data_analysis.py          # Gerador de gráficos de engajamento
│   └── plots/                    # Novas análises (Sunburst, Timeline)
├── dashboard/
│   └── app.py                    # Dashboard Pro com filtros e simulador de IA
└── README_SPRINT3.md             # Este arquivo
```

---

# EDUBOT - Sprint 3: Inteligência Preditiva e Engajamento Avançado
### Challenge FlexMedia - Sprint 3
**Tecnólogo em Inteligência Artificial - FIAP** *"Modelagem de dados complexos e predição de engajamento em tempo real"*

**Repositório:** [https://github.com/Pedrolopesh/farm-tech](https://github.com/Pedrolopesh/farm-tech)

---

## 📋 Índice
1. [Visão Geral da Sprint 3](#-visão-geral-da-sprint-3)
2. [Fluxo de Dados](#-fluxo-de-dados)
3. [Dados Coletados e Simulados](#-dados-coletados-e-simulados)
4. [Estrutura do Projeto](#-estrutura-do-projeto)
5. [Guia de Execução](#-guia-de-execução)
6. [Machine Learning Avançado](#-machine-learning-avançado)
7. [Dashboard de Monitoramento](#-dashboard-de-monitoramento)
8. [Equipe](#-equipe)

---

## 🎯 Visão Geral da Sprint 3
A Sprint 3 do EDUBOT marca a evolução do sistema de monitoramento para uma plataforma de **Inteligência de Dados**. Expandimos a base de dados para 1.500 registros e introduzimos métricas de comportamento humano (frequência de toques) para classificar o nível de interesse do produtor rural.

---

## 🔄 Fluxo de Dados
```text
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   SIMULAÇÃO     │────▶│  BANCO DADOS    │────▶│    ANÁLISE      │
│ 1500 registros  │     │    SQLite       │     │   EDA + Plots   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                       │
         ┌─────────────────────────────────────────────┘
         ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  MACHINE LEARN  │────▶│    MODELO       │────▶│   DASHBOARD     │
│  Random Forest  │     │  (modelo.pkl)   │     │   Streamlit     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```
### Dados Coletados/Simulados

| Campo | Tipo | Descrição |
| :--- | :--- | :--- |
| **timestamp** | DATETIME | Data e hora da interação (Simulado 2025-2026) |
| **session_id** | TEXT | ID único da sessão (UUID) |
| **status_ativacao** | INTEGER | Sensor ativado (1) ou Standby (0) |
| **tempo_permanencia_seg** | INTEGER | Tempo total da interação em segundos |
| **toques_por_minuto** | FLOAT | Frequência de toques na tela por minuto |
| **velocidade_toques** | TEXT | Classificação do ritmo (lenta, média, alta) |
| **tipo_interacao** | TEXT | **Target:** Classificação da experiência (curta/média/longa) |

## 🚀 Guia de Execução

### Pré-requisitos

```bash
# Python 3.11 ou superior
python --version

## 🚀 Instalação
# Navegar até o diretório do projeto
cd challenge-flexmidia

# Instalar dependências
pip install streamlit plotly scikit-learn joblib pandas

### Execução Passo a Passo
#### 1️⃣ Gerar Dados Simulados
```bash
python sensors_simulation/simulated_sensors.py

**Saída esperada:**
```
🚀 Iniciando simulação de dados do EDUBOT v3.0...
✅ 1500 registros gerados com sucesso (Período: 2025-2026)!
💾 Dataset salvo em: sensors_simulation/edubot_sensor_data.csv
```
#### 2️⃣ Inicializar Banco de Dados

```bash
python database/init_db.py
```

**Saída esperada:**
```
🗃️  Atualizando banco de dados SQLite...
✅ Banco de dados sincronizado em: database/totem.db
📥 Carregando 1500 registros para o banco...
✅ Sucesso!

```

#### 3️⃣ Executar Análise de Dados

```bash
python analysis/data_analysis.py
```

**Saída esperada:**
```
📥 Carregando dados do banco de dados...
✅ 1500 registros carregados
📊 Gerando gráficos avançados...
   ✅ sunburst_engajamento.png
   ✅ interacoes_timeline.png
```
#### 4️⃣Executar Análise de Dados
```bash
python ml_model/train_model.py

**Saída esperada:**
🤖 Treinando modelos de Inteligência Preditiva...
✅ Treinamento concluído!
🎯 Acurácia do modelo: 100.00%
💾 Modelo salvo com sucesso em: ml_model/modelo_edubot.pkl
```
#### 5️⃣ Iniciar Dashboard
```bash
streamlit run dashboard/app.py
```
**Acesse:** http://localhost:8501
**Network URL**: http://172.20.10.3:8501

---

## 🔧 Componentes do Sistema
### 1. Simulação de Sensores (`sensors_simulation/`)
O script `simulated_sensors.py` gera 1.500 registros focados em engajamento humano:

- **Volume:** Base de dados robusta para análise de comportamento.

-**Métricas:** Introdução de toques_por_minuto para medir a intensidade da interação.

-**Categorias:**

- Curta: 10-60s

- Média: 61-150s (Nova categoria Sprint 3)

- Longa: 151-300s

### 2. Banco de Dados (`database/`)
 **Schema da tabela interacoes (v3.0):**
 **SQL**
```
 CREATE TABLE interacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME NOT NULL,
    session_id TEXT NOT NULL UNIQUE,
    tempo_permanencia_seg INTEGER NOT NULL,
    toques_por_minuto FLOAT NOT NULL,
    velocidade_toques TEXT NOT NULL,
    status_ativacao INTEGER DEFAULT 1,
    tipo_interacao TEXT NOT NULL
);
```
### 3. Análise de Dados (`analysis/`)
O script `data_analysis.py` agora foca em **Insights de Comportamento:**

- Análise de Ritmo: Identifica se o usuário possui alta ou baixa interação com a interface.

- Visualizações: Gráfico Sunburst para relação entre tempo e velocidade de toques.

---
## 🤖 Machine Learning

### Objetivo
Classificar o perfil de engajamento (`curta, média ou longa`) do produtor rural baseado na intensidade de uso do totem.

### Features Utilizadas

| Feature                | Descrição                 | Tipo |
|------------------------|---------------------------|------|
| `tempo_permanencia_seg`| Duração da sessão         | Numérico |
| toques_por_minuto      | Intensidade da interação  | Numérico |

### Métricas do Modelo Selecionado (Random Forest)
| Métrica   | Valor |
|-----------|-------|
| Acurácia	 | 100%  |
| Precisão	 | 100%  |
| F1-Score	 | 1.0   |

### 📊 Dashboard
O dashboard Streamlit v3.0 oferece uma visão gerencial completa:

***KPIs Principais***
- Total de Sessões Filtradas
- Tempo Médio de Uso
- Intensidade Média de Toques
- % de Engajamento por Categoria

***Visualizações***
- Timeline de acessos (2025-2026)
- Sunburst Chart de Engajamento
- Tabela de logs detalhada em tempo real

***Filtros Avançados***
- Calendário: Seleção de período específico para análise.
- Engajamento: Filtro por tipo de interação e velocidade de toque.

***Seção de IA***
- Simulador interativo onde o gestor pode inserir dados manuais para testar a predição do modelo `.pkl.`

---

### 📐 Diagramas ###
***Arquitetura Sprint 3***
```bash
Snippet de código
flowchart TB
    SIMULACAO[Simulação 1500 registros] --> DATABASE[(SQLite Totem DB)]
    DATABASE --> ANALYSIS[EDA & Insights]
    ANALYSIS --> ML[Random Forest Model]
    ML --> DASHBOARD[Streamlit UI]
```
---

### 📈 Resultados e Métricas ###
***Estatísticas do Dataset (Sprint 3)***

| Métrica                  | Valor    |
|--------------------------|----------|
| Total de registros       | 	1500  |
 Interações Médias	       | ~31%     |
 Interações Longas	       | ~34%     |
 Acurácia do Modelo	100%   | 100%     |

---

## 👥 Equipe

| Nome | RM | Responsabilidade |
|------|-----|------------------|
| Fabrício Mouzer Brito | RM566777 | Documentação Técnica |
| Pedro Henrique Lopes dos Santos | RM568359 | Arquitetura e Diagramas |
| Enzo Nunes Castanheira Gloria da Silva | RM567599 | Estratégia de Dados |
| Larissa Nunes Moreira Reis | RM568280 | Acessibilidade e LGPD |
| Gabriel Rapozo Guimarães Soares | RM568480 | Tecnologias e IA |

**Turma:** R  
**Instituição:** FIAP - Tecnólogo em Inteligência Artificial  
**Data:** Março de 2026

---

## 📄 Licença

Este projeto é desenvolvido para fins acadêmicos como parte do Challenge FlexMedia da FIAP.

---

**Última atualização:** Março de 2026
**Versão:** Sprint 3.0

