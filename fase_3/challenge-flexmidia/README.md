# EDUBOT - Totem Inteligente Acessível para Ambientes Educacionais

**Challenge FlexMedia - Sprint 1**

**Tecnólogo em Inteligência Artificial - FIAP**

*"Democratizando o acesso à informação educacional através da IA"*

---

## 👥 Informações do Projeto

### Equipe

| Nome | RM | E-mail | Responsabilidade |
|------|-----|--------|------------------|
| **Fabrício Mouzer Brito** | 566777 | fabriciomouzer@hotmail.com | Documentação Técnica no GitHub |
| **Pedro Henrique Lopes dos Santos** | - | pedrolopeshls99@gmail.com | Arquitetura e Diagramas |
| **Enzo Nunes Castanheira Gloria da Silva** | - | enzoncgs@gmail.com | Estratégia de Coleta de Dados |
| **Larissa Nunes Moreira Reis** | - | larissa.nmreis@gmail.com | Acessibilidade e LGPD |
| **Gabriel Rapozo Guimarães Soares** | - | rapozogabriel8@gmail.com | Tecnologias e Integração de IA |

**Turma:** R  
**Data:** Outubro de 2025  
**Instituição:** FIAP - Tecnólogo em Inteligência Artificial

---

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Justificativa do Problema](#justificativa-do-problema)
3. [Descrição da Solução](#descrição-da-solução)
4. [Funcionalidades Principais](#funcionalidades-principais)
5. [Tecnologias Utilizadas](#tecnologias-utilizadas)
6. [Arquitetura da Solução](#arquitetura-da-solução)
7. [Estratégia de Coleta de Dados](#estratégia-de-coleta-de-dados)
8. [Segurança e Privacidade (LGPD)](#segurança-e-privacidade-lgpd)
9. [Acessibilidade Universal](#acessibilidade-universal)
10. [Plano de Desenvolvimento](#plano-de-desenvolvimento)
11. [Casos de Uso](#casos-de-uso)
12. [Referências](#referências)
---

## 🎯 Visão Geral

O EDUBOT é um totem inteligente com Inteligência Artificial projetado para ambientes educacionais, com foco em acessibilidade, interação natural por voz e suporte automatizado a consultas acadêmicas. A solução visa facilitar o acesso à informação institucional, reduzir demandas repetitivas nas secretarias e oferecer uma experiência inclusiva para todos os estudantes, incluindo pessoas com deficiência.

O sistema integra hardware embarcado, serviços em nuvem e modelos de IA para entregar informações em tempo real por meio de interface multimodal (voz e tela), garantindo uma experiência intuitiva, personalizada e alinhada às melhores práticas de privacidade e segurança.

---

## 📊 Justificativa do Problema

Ambientes educacionais frequentemente enfrentam desafios como:
- Dificuldade no acesso rápido a informações acadêmicas importantes 
- Falta de recursos acessíveis para alunos com diferentes necessidades 
- Sobrecarga de atendimento presencial em secretarias e pontos de informação 
- Baixa coleta de dados sobre dúvidas e demandas dos estudantes 
- Tais fatores impactam a experiência estudantil e a eficiência institucional.

Com a adoção de um totem inteligente, a instituição passa a oferecer atendimento contínuo, acessível e automatizado, ampliando inclusão, otimização de processos e uso estratégico de dados para melhoria contínua dos serviços educacionais.

---

## 💡 Descrição da Solução

O EDUBOT consiste em um totem físico equipado com IA, sensores e interface interativa capaz de:
- Receber comandos de voz ou toque 
- Processar perguntas e fornecer respostas imediatas relacionadas ao ambiente educacional 
- Oferecer acessibilidade ampliada por meio de áudio, texto e comandos por voz 
- Registrar métricas de uso de forma anonimizada para apoio à gestão

A solução integra um backend em nuvem com APIs e modelos de IA para processamento das solicitações. O sistema foi projetado com foco em:
- Interatividade intuitiva 
- Acessibilidade universal 
- Segurança e privacidade (conformidade LGPD)
- Escalabilidade para diferentes instituições e contextos

Este documento apresenta a arquitetura inicial, tecnologias envolvidas e estratégia para desenvolvimento incremental da solução.

### Diferenciais

- ✅ **Acessibilidade Total:** Conformidade com Lei 13.146/2015
- ✅ **Interação por Voz:** Detecção de voz como funcionalidade principal
- ✅ **IA Conversacional:** Respostas inteligentes e contextualizadas
- ✅ **Privacidade:** Conformidade total com LGPD
- ✅ **Escalabilidade:** Solução replicável em múltiplas instituições

---

## ⚙️ Funcionalidades Principais

### 1. Consultas Acadêmicas por Voz

- Horários de aulas e provas
- Avisos e comunicados institucionais
- Prazos acadêmicos e calendário
- Localização de salas e laboratórios

### 2. Assistente Virtual Inteligente

- Respostas contextualizadas usando IA
- Compreensão de linguagem natural
- Personalização baseada no perfil do estudante
- Suporte multilíngue (Português, Inglês, Libras)

### 3. Acessibilidade

- **Cognitiva:** Linguagem simplificada, navegação intuitiva
- **Motora:** Comandos por voz, botões grandes e espaçados

### 4. Dashboard Institucional

- Visualização de métricas de uso
- Análise de perguntas frequentes
- Relatórios de satisfação dos estudantes

---
## 🛠️ Tecnologias Utilizadas

As tecnologias abaixo foram selecionadas considerando acessibilidade, escalabilidade, segurança e viabilidade para a Sprint 1.

### Linguagens e Frameworks
- Python 3.11+
- FastAPI (APIs REST)
- JavaScript/TypeScript
- HTML e CSS (prototipação)

### Inteligência Artificial
- GPT-4 / Gemini (Processamento de linguagem natural)
- Whisper (Speech-to-Text)
- Google Text-to-Speech (acessibilidade por áudio)
- Scikit-learn (análises futuras)

### Infraestrutura e Banco de Dados
- Supabase (PostgreSQL + Auth + Storage)
- Google Cloud (execução e monitoramento)
- n8n (integrações e automações)

### Hardware
- Tela touchscreen
- Microfone e alto-falantes
- ESP32 (detecção de presença e ativação)

### Ferramentas de Apoio
- Lovable (prototipação rápida)
- Git / GitHub (versionamento)
- Markdown (documentação)


---

## 🏗️ Arquitetura da Solução

A arquitetura do EDUBOT foi planejada para garantir modularidade, segurança, acessibilidade e integração entre hardware embarcado, serviços em nuvem e IA generativa.

### Visão Geral
Usuário → Totem (Tela + Microfone)
        → API Backend (FastAPI)
        → Serviços de IA (LLMs + STT + TTS)
        → Banco de Dados (Supabase)
        → Dashboard Institucional

### 🧩 Componentes Principais

| Camada | Função | Tecnologias |
|--------|--------|------------|
| Interface do Totem | Interação via voz e toque | Tela touch, microfone, alto-falantes |
| Backend | Processamento, lógica e orquestração | Python, FastAPI, APIs REST |
| Inteligência Artificial | Interpretação e respostas naturais | Whisper, GPT-4/Gemini, TTS |
| Banco de Dados | Persistência e análises | Supabase (PostgreSQL) |
| Monitoramento e Analytics | Métricas de uso e insights | Dashboard, logs de uso |

### Fluxo Simplificado

1. Usuário interage com o totem (voz ou toque).
2. Backend recebe a solicitação.
3. Serviços de IA interpretam e geram resposta.
4. Resposta apresentada na tela e áudio.
5. Dados de uso armazenados conforme LGPD. 
6. Dashboard para gestão e insights.

### Diagramas Detalhados
TODO: PREENCHER COM DIAGRAMA

---
## 📱 Casos de Uso

### UC01 — Consultar Informações Acadêmicas

**Ator:** Estudante  
**Objetivo:** Obter horários, calendários e avisos  
**Interação:** Voz ou toque  
**Resultado:** Resposta exibida na tela e narrada em áudio  

Exemplo: "Qual é meu horário de aula hoje?"

---

### UC02 — Acessibilidade para Deficiência Visual

**Ator:** Estudante com deficiência visual  
**Objetivo:** Obter informações sem barreiras  
**Interação:** Comandos de voz + feedback em áudio  
**Recurso:** Ativação automática ao detectar presença  

Exemplo: "Onde fica a biblioteca?"

---

### UC03 — Avaliar Atendimento

**Ator:** Todos os usuários  
**Objetivo:** Registrar satisfação e experiência  
**Interação:** Avaliação 1–5 e comentário  
**Uso:** Métricas e melhorias contínuas

---

### UC04 — Informações para Visitantes

**Ator:** Visitantes do campus  
**Objetivo:** Informações gerais e localização  
**Interação:** Toque ou voz  
**Resultado:** Orientações no mapa e áudio

### Diagramas Detalhados
TODO: PREENCHER COM DIAGRAMA

---

## 📊 Estratégia de Coleta de Dados
## Estratégia de Coleta de Dados

O **EDUBOT** atua não apenas como ponto de informação, mas também como ferramenta de inteligência para apoiar a gestão educacional e a melhoria contínua da experiência dos estudantes. A coleta de dados será realizada de forma **anonimizada** e em conformidade com a **LGPD**, visando compreender padrões de uso, preferências dos usuários e eficiência da solução.

### Tipos de Dados Coletados

| Categoria              | Exemplos                                            | Finalidade                                   |
|-----------------------|------------------------------------------------------|----------------------------------------------|
| Perfil de uso (opcional e anônimo) | Idioma preferido, tipo de usuário (aluno/visitante) | Personalizar acesso e conteúdo               |
| Interação             | Tempo de interação, perguntas realizadas, voz/toque  | Medir fluidez e eficiência                   |
| Engajamento           | Nº de interações, taxa de conclusão, tempo médio     | Identificar padrões e demandas               |
| Satisfação            | Avaliação rápida (1 a 5) e comentários               | Monitorar qualidade do atendimento           |
| Desempenho técnico    | Horários de uso, erros, tempo de resposta            | Otimizar performance e suporte               |

### Objetivos da Coleta

- Identificar as principais demandas dos estudantes.  
- Ajustar a interface e os recursos de acessibilidade.  
- Melhorar a precisão e a relevância das respostas da IA.  
- Planejar infraestrutura com base em horários de pico.  
- Monitorar continuamente a satisfação do usuário.  
- Gerar insights para apoio às decisões institucionais.

### Privacidade e Segurança

- Coleta mínima necessária.  
- Dados tratados apenas de forma agregada e anonimizada.  
- Aviso de coleta exibido no primeiro uso.  
- Armazenamento seguro com acesso restrito.  
- Conformidade com a LGPD em todas as etapas.

### Conformidade LGPD

- ✅ **Minimização:** Apenas dados essenciais são coletados
- ✅ **Anonimização:** Dados pessoais são anonimizados
- ✅ **Consentimento:** Aviso de coleta exibido no primeiro uso
- ✅ **Transparência:** Política de privacidade acessível
- ✅ **Segurança:** Criptografia e controle de acesso

---

## 🔒 Segurança e Privacidade (LGPD)

O EDUBOT segue os princípios da Lei Geral de Proteção de Dados (LGPD), garantindo transparência, segurança e ética no tratamento das informações.

### Diretrizes
- Dados coletados apenas para fins acadêmicos e melhoria do serviço
- Princípio da minimização: somente dados necessários
- Consentimento informado quando aplicável
- Dados sensíveis tratados com criptografia e controles rígidos

### Medidas de Segurança
- Criptografia em trânsito e repouso
- Controle de acesso por permissões
- Auditoria e monitoramento de logs
- Procedimentos para notificações de incidentes

### Conformidade Garantida
- Finalidade específica e legítima
- Transparência ao usuário
- Retenção e descarte seguro dos dados

---
## 🗂️ Plano de Desenvolvimento

### Fases do Projeto

| Fase | Objetivo | Entregas |
|---|---|---|
Planejamento | Definir escopo e arquitetura | Documentação e diagramas |
Backend e IA | Implementar APIs e conexão com IA | API funcional + POC IA |
Interface e Acessibilidade | Prototipar interface e comandos por voz | UI funcional e acessível |
Hardware | Integrar ESP32 ao fluxo | Totem com sensores funcionais |
Coleta e Dashboard | Registrar interações e exibir métricas | Registro de dados + dashboards |
Testes | Validação e ajustes | Protótipo funcional para demonstração |

### Metodologia
- Abordagem ágil
- Entregas incrementais
- Feedback contínuo
- Validação com usuários simulados

### Responsabilidades da Equipe

| Membro | Responsabilidades |
|--------|------------------|
Fabrício | Backend, IA, documentação técnica |
Pedro | Arquitetura, diagramas e infraestrutura |
Enzo | Estratégia e modelagem de dados |
Larissa | LGPD, acessibilidade e compliance |
Gabriel | Interface, integração e hardware |

A equipe atuará de forma colaborativa revisando entregas e garantindo consistência técnica.

---

### Divisão de Responsabilidades

**Fabrício Mouzer Brito (RM 566777):**
- Arquitetura geral do sistema
- Desenvolvimento backend (API, IA, banco de dados)
- Integração de serviços de IA (OpenAI, Whisper)
- Segurança e conformidade LGPD
- Documentação técnica
- Coordenação do projeto

> **Nota:** Como projeto individual, todas as responsabilidades são do aluno. Em caso de formação de equipe futura, as responsabilidades serão redistribuídas.

---

## 🏆 Diferenciais Competitivos

1. **Acessibilidade Total:** Conformidade completa com Lei 13.146/2015 e WCAG 2.1
2. **Interação por Voz:** Reconhecimento de voz como funcionalidade principal
3. **IA Conversacional:** Respostas inteligentes e contextualizadas
4. **Privacidade Garantida:** Conformidade total com LGPD
5. **Escalabilidade:** Solução replicável em milhares de instituições
6. **Analytics Institucional:** Dashboard com métricas valiosas
7. **Baixo Custo:** Uso de APIs com IA

---

## 📚 Referências

### Legislação

1. **Lei 13.146/2015** - Lei Brasileira de Inclusão da Pessoa com Deficiência (LBI)  
   [http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm)

2. **Lei 13.709/2018** - Lei Geral de Proteção de Dados (LGPD)  
   [http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)

### Normas e Diretrizes

3. **WCAG 2.1** - Web Content Accessibility Guidelines  
   [https://www.w3.org/WAI/WCAG21/quickref/](https://www.w3.org/WAI/WCAG21/quickref/)

4. **NBR 9050:2020** - Acessibilidade a edificações, mobiliário, espaços e equipamentos urbanos  
   [https://www.abnt.org.br/](https://www.abnt.org.br/)

### Dados e Estatísticas

5. **Censo da Educação Superior 2022** - INEP  
   [https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-da-educacao-superior](https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-da-educacao-superior)

6. **Censo Demográfico 2019** - IBGE (Pessoas com Deficiência)  
   [https://www.ibge.gov.br/](https://www.ibge.gov.br/)

### Tecnologias

7. **OpenAI API Documentation**  
   [https://platform.openai.com/docs](https://platform.openai.com/docs)

8. **Whisper (Speech Recognition)**  
   [https://openai.com/research/whisper](https://openai.com/research/whisper)

9. **Supabase Documentation**  
   [https://supabase.com/docs](https://supabase.com/docs)

10. **FastAPI Documentation**  
    [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

11. **ESP32 Documentation**  
    [https://docs.espressif.com/projects/esp-idf/en/latest/esp32/](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)

12. **Iovable Platform**  
    [https://iovable.com/](https://iovable.com/)

### Acessibilidade

13. **VLibras** - Tradutor de Português para Libras  
    [https://www.gov.br/governodigital/pt-br/vlibras](https://www.gov.br/governodigital/pt-br/vlibras)

14. **Hand Talk** - Tradução em Libras  
    [https://www.handtalk.me/](https://www.handtalk.me/)

### Artigos e Pesquisas

15. **Acessibilidade Digital no Ensino Superior** - Revista Brasileira de Educação Especial  
    [https://www.scielo.br/](https://www.scielo.br/)

16. **IA e Educação Inclusiva** - UNESCO  
    [https://www.unesco.org/](https://www.unesco.org/)

---

## 📞 Contato

### Equipe do Projeto

| Nome | E-mail | Responsabilidade |
|------|--------|------------------|
| Fabrício Mouzer Brito | fabriciomouzer@hotmail.com | Documentação Técnica no GitHub |
| Pedro Henrique Lopes dos Santos | pedrolopeshls99@gmail.com | Arquitetura e Diagramas |
| Enzo Nunes Castanheira Gloria da Silva | enzoncgs@gmail.com | Estratégia de Coleta de Dados |
| Larissa Nunes Moreira Reis | larissa.nmreis@gmail.com | Acessibilidade e LGPD |
| Gabriel Rapozo Guimarães Soares | rapozogabriel8@gmail.com | Tecnologias e Integração de IA |

**Turma:** R  
**Instituição:** FIAP - Faculdade de Informática e Administração Paulista  
**Curso:** Tecnólogo em Inteligência Artificial

---

## 📄 Licença

Este projeto é desenvolvido para fins acadêmicos como parte do Challenge FlexMedia da FIAP.

---

**Última atualização:** Outubro de 2025  
**Versão:** 3.0 (Simplificada)
