# EDUBOT - Sprint 4: IA Visual e Dashboard Interativo
### Challenge FlexMedia - Sprint 4
**Tecnólogo em Inteligência Artificial - FIAP** 
*"Visão Computacional Simulada, Modelos Realistas e Acessibilidade"*

---

## 🎯 Visão Geral da Sprint 4
A Sprint 4 do EDUBOT avança na inteligência do totem, integrando uma simulação de IA Visual, corrigindo problemas de Data Leakage para obter métricas mais realistas, e expandindo o foco em Acessibilidade e Conformidade Legal (LGPD e LBI).

### Principais Novidades
* ✅ **IA Visual Simulada:** Detecção de perfil e humor do usuário para adaptar o conteúdo e prever o engajamento.
* ✅ **Modelo de ML Realista:** Correção de *Data Leakage*, resultando em uma acurácia real e confiável de 79%.
* ✅ **Dashboard Interativo Avançado:** Inclusão de um simulador de IA e novas visualizações (Heatmap e Sunburst).
* ✅ **Acessibilidade e Compliance:** Documentação focada na Lei Brasileira de Inclusão (LBI) e Lei Geral de Proteção de Dados (LGPD).

---

## 📸 IA Visual Simulada (Objetivo 2)
Nesta sprint, implementamos um conceito de Visão Computacional para o totem, capaz de estimar o humor e o nível de atenção do usuário para personalizar o engajamento:
* **Focado:** O usuário mantém contato visual constante com o totem. O sistema sugere interações mais densas e longas.
* **Distraído:** O usuário olha frequentemente para os lados ou para o celular. O sistema tenta recapturar a atenção com conteúdos curtos e interativos.
* **Ausente:** O usuário se afastou do totem. O sistema encerra a sessão ou entra em modo de espera.

---

## 🤖 Machine Learning e Métricas (Objetivo 3)

### Correção de Data Leakage
Nas sprints anteriores, o modelo apresentava 100% de acurácia, o que indicava um problema de *Data Leakage* (vazamento de dados), pois a variável `tempo_permanencia_seg` estava sendo usada para prever o próprio engajamento (duração da interação). 
Nesta sprint, o modelo foi reestruturado para usar apenas o **comportamento** (toques por minuto, perfil e humor) para prever o engajamento de forma realista.

### Métricas Reais do Modelo (`modelo_edubot_v4.pkl`)
| Métrica   | Valor |
|-----------|-------|
| Acurácia	 | 79%   |

O modelo foi treinado através do script `ml_model/train_model.py` e é consumido pelo `dashboard/app.py` e pela API.

---

## 📊 Dashboard e Análise de Dados (Objetivo 5)
O Dashboard (`dashboard/app.py`) foi atualizado para incluir:
- **Simulador de IA Visual:** Uma barra lateral onde é possível testar as predições do modelo em tempo real, selecionando o Perfil, Humor e Intensidade de toques.
- **Gráfico Sunburst:** Visualiza a relação hierárquica entre o perfil do usuário, o humor estimado e o tipo de interação resultante.
- **Heatmap (Mapa de Calor):** Gerado pelo script `analysis/data_analysis.py`, ilustra a relação e frequência entre o perfil do usuário e seu humor durante o uso do totem.

---

## 🔒 Acessibilidade e Conformidade Legal

### Lei Brasileira de Inclusão (LBI - Lei 13.146/2015)
O projeto EDUBOT foi concebido com base nas diretrizes da LBI, garantindo que o totem seja acessível a todos os estudantes. As interfaces foram projetadas para suportar interação por voz, audiodescrição e ajustes de contraste, assegurando autonomia e independência para pessoas com deficiência.

### Lei Geral de Proteção de Dados (LGPD - Lei 13.709/2018)
A privacidade dos usuários é garantida por meio da **anonimização total** dos dados coletados. As imagens da IA Visual (simulada) não são armazenadas; apenas os metadados (como humor e perfil estimado) são salvos de forma agregada no banco de dados para geração de métricas institucionais, sem identificar o indivíduo.

---

## 📁 Estrutura do Projeto
```text
challenge-flexmidia/
├── fix_and_populate.py           # Script principal para criar e popular o banco
├── database/
│   └── totem.db                  # Banco de dados populado
├── dashboard/
│   └── app.py                    # Interface Streamlit com simulador de IA e KPIs
├── ml_model/
│   ├── train_model.py            # Treinamento do modelo sem Data Leakage
│   └── modelo_edubot_v4.pkl      # Modelo treinado final (Acurácia: 79%)
├── analysis/
│   └── data_analysis.py          # Script gerador do Heatmap
└── api/
    └── main.py                   # API FastAPI consumindo o modelo de ML
```

### Guia de Execução

1. **Configurar e Popular o Banco de Dados:**
   Execute o script na raiz do projeto para gerar as interações simuladas:
   ```bash
   python fix_and_populate.py
   ```

2. **Iniciar o Dashboard Interativo:**
   ```bash
   streamlit run dashboard/app.py
   ```

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
**Data:** Abril de 2026

---

**Última atualização:** Abril de 2026  
**Versão:** Sprint 4.0
