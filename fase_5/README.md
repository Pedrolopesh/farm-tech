# 🌾 FarmTech Solutions: Inteligência Artificial na Predição de Safras

Este repositório contém a solução de Ciência de Dados desenvolvida para a **FarmTech Solutions**, focada em transformar dados climáticos em inteligência preditiva para o agronegócio. O projeto integra modelos de regressão (supervisionados) e técnicas de agrupamento (não supervisionados).

## Informações do projeto
 Link do repositório: https://github.com/Pedrolopesh/farm-tech/tree/master/fase_5


👨‍🎓 Integrantes:
| Nome | RM | E-mail |
|------|-----|--------|
| **Fabrício Mouzer Brito** | RM566777 | fabriciomouzer@hotmail.com |
| **Pedro Henrique Lopes dos Santos** | RM568359 | pedrolopeshls99@gmail.com |
| **Enzo Nunes Castanheira Gloria da Silva** | RM567599 | enzoncgs@gmail.com |
| **Larissa Nunes Moreira Reis** | RM568280 | larissa.nmreis@gmail.com |
| **Gabriel Rapozo Guimarães Soares** | RM568480 | rapozogabriel8@gmail.com |

## 📋 Visão Geral
O objetivo deste projeto é prever o rendimento agrícola (*Yield*) com base em variáveis como Temperatura, Precipitação e Humidade, além de segmentar a fazenda em zonas de manejo estratégico e identificar anomalias.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.13
* **Bibliotecas:** Pandas, Scikit-Learn, Seaborn, Matplotlib
* **Ferramenta de Desenvolvimento:** VS Code (Jupyter Notebooks)

## 🔬 Etapas do Desenvolvimento

### 1. Análise Exploratória (EDA)
Realizámos uma investigação profunda sobre a integridade dos dados (sem valores nulos) e as correlações entre clima e colheita. Utilizamos matrizes de correlação e *pairplots* para validar os padrões de cada cultura (Arroz, Milho, etc.).

### 2. Modelagem Supervisionada (Fase 4)
Implementámos **cinco algoritmos diferentes** para garantir a melhor escolha técnica na previsão do rendimento. Os resultados obtidos foram:

| Algoritmo | R² Score (Acurácia) | MAE (Erro Médio) |
| :--- | :--- | :--- |
| **Regressão Linear** | **0.9950** | 3137.94 |
| **Regressão Ridge** | 0.9950 | 3138.07 |
| **Regressão Lasso** | 0.9950 | 3138.40 |
| **Random Forest** | 0.9947 | **2802.37** |
| **Decision Tree** | 0.9934 | 4454.49 |

**Análise:** A **Regressão Linear** obteve a melhor acurácia estatística geral, enquanto o **Random Forest** apresentou o menor erro absoluto (MAE), sendo o mais preciso em valores reais.

### 3. Modelagem Não Supervisionada (Capítulo 10)
Para além da predição, aplicámos técnicas para descobrir padrões ocultos:
* **K-Means:** Segmentação em **3 Zonas de Manejo**, permitindo a aplicação variável de recursos.
* **DBSCAN:** Identificação de **outliers** (ruídos climáticos) por densidade.
* **PCA:** Redução de dimensionalidade para visualização gráfica dos agrupamentos em 2D.

## 📊 Conclusões e Limitações
* **Pontos Fortes:** O modelo atingiu uma precisão superior a 99%, permitindo um planeamento financeiro seguro. A deteção de anomalias via DBSCAN evita que dados corrompidos influenciem a tomada de decisão.
* **Limitações:** O modelo atual foca-se apenas em variáveis climáticas. A inclusão de dados sobre nutrientes do solo e pragas poderia aumentar ainda mais a robustez.

## 🛠️ Como Executar o Projeto
1. Clone o repositório.
2. Certifique-se de que o arquivo `crop_yield.csv` está na mesma pasta que o notebook.
3. Instale as dependências:
   ```bash
   pip install pandas scikit-learn seaborn matplotlib
4. Em caso de dificuldade de visualizar no Jupyter, considerar pelo URL abaixo:
   https://nbviewer.org/github/Pedrolopesh/farm-tech/blob/master/fase_5/Entrega_FarmTech.ipynb

   
## ☁️ Entrega 2: Arquitetura e Estimativa de Custos (AWS)


## 📝 Descrição da Infraestrutura
Para a hospedagem da API de Machine Learning da **FarmTech Solutions**, realizamos uma estimativa de custos utilizando a **AWS Pricing Calculator**, comparando a viabilidade técnica e financeira entre duas regiões: **N. Virginia (us-east-1)** e **São Paulo (sa-east-1)**.

### Configuração da Infraestrutura
* **Instância:** Linux (t3.micro - 2 vCPUs, 1 GiB RAM)
* **Armazenamento:** 50 GB EBS (gp3)
* **Modelo de Contratação:** On-Demand (100% de uso mensal)

---

## 📊 Comparativo de Custos (Mensal)

| Componente | Região: N. Virgínia (EUA) | Região: São Paulo (Brasil) |
| :--- | :--- | :--- |
| **Instância EC2** | 7.59 USD | 12.26 USD |
| **Armazenamento (EBS)** | 4.00 USD | 7.60 USD |
| **Total Estimado** | **11.59 USD** | **19.86 USD** |

---

## ⚖️ Justificativa de Escolha: São Paulo (sa-east-1)

Embora a região da Virgínia apresente um custo inferior, a escolha estratégica para este projeto é a região de **São Paulo**, baseada nos seguintes pilares:

1. **Baixa Latência:** Como os sensores e os usuários finais (fazenda) estão localizados no Brasil, o processamento local garante uma resposta em tempo real para as predições de safra.
2. **Conformidade Legal (LGPD):** A manutenção dos dados em solo nacional atende às exigências da Lei Geral de Proteção de Dados, evitando riscos jurídicos associados à transferência internacional de dados sensíveis da operação agrícola.
3. **Soberania Digital:** Garantia de que a infraestrutura crítica do cliente (FarmTech) opere sob a jurisdição brasileira.

---

## 🖼️ Evidências da Configuração (N. Virgínia - Referência de Preço Base)

Abaixo estão os detalhes da configuração realizada na calculadora da AWS que serviu de base para o comparativo de menor custo.

#### 1. Especificações da Instância EC2
![Configuração da Instância](./assets/Captura%20de%20tela%202026-03-18%20015300.png)

#### 2. Detalhes de Armazenamento (EBS)
![Configuração de Armazenamento](./assets/Captura%20de%20tela%202026-03-18%20015333.png)

#### 3. Resumo do Custo Mensal Total
![Resumo de Custos](./assets/Captura%20de%20tela%202026-03-18%20014707.png)

---

## 🖼️ Evidências da Configuração (São Paulo - Referência de Preço Base)

Abaixo estão os detalhes da configuração realizada na calculadora da AWS que serviu de base para o comparativo de menor custo.

#### 1. Especificações da Instância EC2
![Configuração da Instância](./assets/Captura%20de%20tela%202026-03-18%20015300.png)

#### 2. Detalhes de Armazenamento (EBS)
![Configuração de Armazenamento](./assets/Captura%20de%20tela%202026-03-18%20015333.png)

#### 3. Resumo do Custo Mensal Total
![Resumo de Custos](./assets/Captura%20de%20tela%202026-03-18%20022632.png)
---

### 💡 Próximos Passos
* [ ] Realizar o deploy da API na instância configurada.
* [ ] Configurar as Security Groups para acesso seguro à API.
* [ ] Validar a latência de resposta entre a aplicação e a infraestrutura em SP.

---

> **Nota:** Os valores apresentados são estimativas baseadas na tabela oficial da AWS de Março de 2026 e podem variar conforme o uso real de transferência de dados (Data Transfer Out).
