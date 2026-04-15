# Diagramas Sprint 2 - EDUBOT

Este diretório contém os diagramas técnicos da Sprint 2 do projeto EDUBOT.

## Arquivos

### 1. `arquitetura-sprint2.mmd`
Diagrama de arquitetura geral do sistema implementado na Sprint 2, mostrando:
- Componentes do totem físico (futuro)
- Pipeline de simulação de dados
- Banco de dados SQLite
- Módulo de análise
- Pipeline de Machine Learning
- Dashboard Streamlit

### 2. `fluxo-dados-sprint2.mmd`
Diagrama do fluxo de dados desde a entrada até a saída:
- Entrada de dados (sensores ou simulação)
- Coleta de métricas
- Armazenamento em SQLite
- Processamento e limpeza
- Análise e visualização
- Machine Learning
- Saídas (dashboard, gráficos, predições)

### 3. `pipeline-ml-sprint2.mmd`
Diagrama detalhado do pipeline de Machine Learning:
- Features utilizadas
- Preparação de dados
- Modelos treinados (Decision Tree e Random Forest)
- Métricas de avaliação
- Deploy do modelo

## Como Visualizar

### Opção 1: Mermaid Live Editor
1. Acesse [Mermaid Live Editor](https://mermaid.live/)
2. Cole o conteúdo do arquivo `.mmd`
3. Visualize e exporte como PNG/SVG

### Opção 2: VS Code
1. Instale a extensão "Mermaid Preview"
2. Abra o arquivo `.mmd`
3. Use `Ctrl+Shift+V` para preview

### Opção 3: GitHub
Os arquivos `.mmd` são renderizados automaticamente no GitHub.

## Legendas de Cores

| Cor | Significado |
|-----|-------------|
| 🔵 Azul claro | Hardware/Entrada |
| 🟢 Verde claro | Dados/Armazenamento |
| 🟠 Laranja claro | Processamento |
| 🔴 Rosa claro | Machine Learning |
| 🟣 Roxo claro | Dashboard/Saída |
| 🔷 Ciano claro | Output Final |
