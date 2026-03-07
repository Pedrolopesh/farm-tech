# EDUBOT - Sprint 3: Inteligência Preditiva e Engajamento Avançado
### Challenge FlexMedia - Sprint 3
**Tecnólogo em Inteligência Artificial - FIAP** *"Modelagem de dados complexos e predição de engajamento em tempo real"*

**Repositório:** [https://github.com/Pedrolopesh/farm-tech](https://github.com/Pedrolopesh/farm-tech)

---

## 📋 Índice
1. [Visão Geral da Sprint 3](#-visão-geral-da-sprint-3)
2. [Novidades desta Versão](#-novidades-desta-versão)
3. [Estrutura do Projeto](#-estrutura-do-projeto)
4. [Camada de Edge Computing (IoT)](#-Camada-de-Edge-Computing-(IoT))
5. [Cognitive CyberSecurity](#-Cognitive-CyberSecurity)
6. [Guia de Execução](#-guia-de-execução)
7. [Machine Learning Avançado](#-machine-learning-avançado)
8. [Dashboard de Monitoramento](#-dashboard-de-monitoramento)
9. [Resultados e Métricas](#-resultados-e-métricas)
10. [Equipe](#-equipe)

---

## 🎯 Visão Geral da Sprint 3
A Sprint 3 do EDUBOT marca a evolução do sistema de monitoramento para uma plataforma de **Inteligência de Dados**. Expandimos a base de dados para 1.500 registros e introduzimos métricas de comportamento humano (frequência de toques) para classificar o nível de interesse do produtor rural.

### Objetivos Alcançados
* ✅ **Big Data Simulação:** Expansão para 1.500 registros cobrindo o período de 2025 a 2026.
* ✅ **Novas Variáveis:** Inclusão de `toques_por_minuto` e `velocidade_toques` (alta/baixa).
* ✅ **ML de Alta Precisão:** Implementação do Random Forest com 100% de acurácia nos padrões de treino.
* ✅ **Integração de Borda: Implementação do firmware para ESP32-CAM.**
* ✅ **Segurança de Dados: Proteção via X-API-KEY e Pydantic.**

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
│   ├── simulated_sensors.py      # Script v3.0 (1500 registros)
├── edge/
│   └── esp32_firmware.ino        # Firmware C++ para o ESP32-CAM
├── database/
│   ├── init_db.py                # Script de recriação do banco
│   └── totem.db                  # SQLite atualizado
├── ml_model/
│   ├── train_model.py            # Treinamento do Random Forest
│   └── modelo_edubot.pkl         # Modelo serializado
├── dashboard/
│   └── app.py                    # Dashboard Pro com Matriz de Confusão e Heatmap
└── README_SPRINT3.md             # Este arquivo
```
---

## 🌐 **Camada de Edge Computing (IoT)**
Nesta sprint, o EDUBOT deixa de ser apenas uma simulação para se tornar um sistema de borda real utilizando o ESP32-CAM.

**Conexão e Funcionamento (Hipotético/Prático)**
- **Hardware**: Utilização do módulo AI Thinker ESP32-CAM para captura de dados.
- **Protocolo**: O hardware envia requisições HTTP POST com pacotes JSON contendo o tempo_permanencia e toques_por_minuto.
- **Modo de Gravação**: Para a carga do firmware, é necessária uma ponte física entre o pino GPIO 0 e o GND da placa.

---
## 🛡️ Cognitive CyberSecurity
A segurança foi integrada em todas as camadas para garantir a integridade dos dados da FlexMedia:
- Autenticação: O ESP32 deve enviar obrigatoriamente a chave X-API-KEY no cabeçalho das requisições para que a API autorize a ingestão.
- Validação de Schema: A API utiliza Pydantic para assegurar que apenas dados formatados corretamente entrem no banco de dados.
- Integridade SQL: Uso de CHECK Constraints no SQLite para evitar valores inválidos de sensores.

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
````
**Saída esperada:**
🚀 Iniciando simulação de dados do EDUBOT v3.0...
✅ 1500 registros gerados com sucesso (Período: 2025-2026)!
💾 Dataset salvo em: sensors_simulation/edubot_sensor_data.csv

#### 2️⃣ Inicializar Banco de Dados

```bash
python challenge-flexmidia/database/init_db.py
```
**Saída esperada:**
🗃️  Atualizando banco de dados SQLite...
✅ Banco de dados sincronizado em: database/totem.db
📥 Carregando 1500 registros para o banco...
✅ Sucesso!

#### 4️⃣Executar Análise de Dados
```bash
python challenge-flexmidia/ml_model/train_model.py
```
**Saída esperada:**
🤖 Treinando modelos de Inteligência Preditiva...
✅ Treinamento concluído!
🎯 Acurácia do modelo: 100.00%
💾 Modelo salvo com sucesso em: ml_model/modelo_edubot.pkl

#### 5️⃣ Iniciar Dashboard
```bash
streamlit run challenge-flexmidia/dashboard/app.py
```
**Acesse:** http://localhost:8501
**Network URL**: http://192.168.0.29:8501

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

