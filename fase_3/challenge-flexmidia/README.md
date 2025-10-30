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
8. [Segurança e Privacidade](#segurança-e-privacidade)
9. [Acessibilidade Universal](#acessibilidade-universal)
10. [Plano de Desenvolvimento](#plano-de-desenvolvimento)
11. [Casos de Uso](#casos-de-uso)
12. [Referências](#referências)

---

## 🎯 Visão Geral

O **EDUBOT** é um totem inteligente equipado com Inteligência Artificial, projetado para ambientes educacionais como escolas, faculdades e bibliotecas. A solução combina tecnologias de IA com foco total em **acessibilidade universal**, permitindo que todos os estudantes tenham acesso facilitado a informações acadêmicas, horários, avisos e suporte educacional personalizado.

O projeto atende à crescente demanda por soluções tecnológicas inclusivas no ambiente educacional, alinhando-se com a Lei Brasileira de Inclusão (Lei 13.146/2015) e a Lei Geral de Proteção de Dados (LGPD - Lei 13.709/2018).

---

## 📊 Justificativa do Problema

### Contexto Atual

O ambiente educacional brasileiro enfrenta diversos desafios relacionados ao acesso à informação e à inclusão de estudantes com deficiência:

**1. Barreiras de Comunicação**

Estudantes frequentemente enfrentam dificuldades para obter informações básicas como horários de aulas, avisos importantes, localização de salas e serviços acadêmicos. Os métodos tradicionais de comunicação (murais físicos, e-mails institucionais) são ineficientes e não alcançam todos os públicos de forma equitativa.

**2. Exclusão de Pessoas com Deficiência**

Segundo o Censo da Educação Superior 2022 (INEP), apenas 0,56% dos estudantes universitários brasileiros declaram ter alguma deficiência, evidenciando barreiras sistêmicas de acesso à informação e aos serviços educacionais.

**3. Sobrecarga das Secretarias Acadêmicas**

Secretarias e bibliotecas recebem diariamente centenas de consultas repetitivas sobre horários, prazos e procedimentos. Isso sobrecarrega os funcionários e gera filas, reduzindo a eficiência do atendimento.

**4. Falta de Personalização**

Sistemas tradicionais não oferecem personalização baseada no perfil ou necessidades individuais, resultando em experiências genéricas e pouco eficazes.

### Impacto do Problema

- **Exclusão educacional:** Estudantes com deficiência enfrentam barreiras adicionais
- **Ineficiência operacional:** Tempo desperdiçado em consultas repetitivas
- **Experiência comprometida:** Frustração devido à dificuldade de acesso à informação
- **Perda de dados:** Falta de métricas sobre uso de serviços e necessidades dos estudantes

### Oportunidade

A implementação de um totem inteligente com IA e foco em acessibilidade representa uma oportunidade de transformar a experiência educacional, tornando-a mais inclusiva, eficiente e centrada no estudante.

---

## 💡 Descrição da Solução

### O que é o EDUBOT?

O **EDUBOT** é um totem físico interativo equipado com:

- **Display touchscreen** para interação visual
- **Sistema de reconhecimento de voz** (funcionalidade principal)
- **Câmera** para reconhecimento de QR Code
- **Sensores de proximidade** para ativação automática
- **Alto-falantes** para feedback de áudio
- **Conectividade WiFi** para integração com sistemas em nuvem
- **Hardware embarcado** (ESP32 ou similar) para processamento

> **Nota:** As especificações de hardware são conceituais e podem ser ajustadas nas próximas sprints conforme viabilidade técnica e orçamento.

### Como Funciona?

1. **Ativação:** Estudante se aproxima do totem (sensor de proximidade) ou escaneia QR Code
2. **Interação por Voz:** Sistema de reconhecimento de voz permite comandos falados (prioridade)
3. **Processamento IA:** Assistente virtual processa a solicitação usando IA conversacional
4. **Resposta Multimodal:** Informação é apresentada em texto, áudio e/ou visual
5. **Coleta de Dados:** Sistema registra métricas de uso (anonimizadas) para análise

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

### 3. Acessibilidade Universal

- **Visual:** Leitura de tela, alto contraste, ampliação de texto
- **Auditiva:** Legendas, tradução em Libras (futura integração)
- **Cognitiva:** Linguagem simplificada, navegação intuitiva
- **Motora:** Comandos por voz, botões grandes e espaçados

### 4. Coleta de Feedback

- Avaliação de satisfação após cada interação
- Coleta de sugestões e reclamações
- Métricas de uso para melhoria contínua

### 5. Dashboard Institucional

- Visualização de métricas de uso
- Análise de perguntas frequentes
- Relatórios de satisfação dos estudantes
- Identificação de demandas não atendidas

---

## 🛠️ Tecnologias Utilizadas

> **Nota:** As tecnologias listadas são opções planejadas e podem ser ajustadas conforme necessidades e viabilidade nas próximas sprints.

### Linguagens de Programação

- **Python 3.11+:** Backend, IA e processamento de dados
- **JavaScript/TypeScript:** Frontend (se necessário)

### Inteligência Artificial

- **OpenAI GPT-4 / Google Gemini:** IA conversacional
- **Whisper (OpenAI):** Reconhecimento de voz (speech-to-text)
- **Google Text-to-Speech:** Síntese de voz (text-to-speech)
- **Scikit-learn:** Análise de padrões e classificação

### Hardware (Conceitual)

- **ESP32 ou ESP32-CAM:** Microcontrolador com WiFi e câmera
- **Sensores de proximidade:** Detecção de presença
- **Display touchscreen:** Interface visual
- **Microfone e alto-falantes:** Interação por voz

> **Importante:** Especificações técnicas detalhadas de hardware serão definidas na fase de implementação.

### Banco de Dados

- **Supabase (PostgreSQL):** Armazenamento de dados estruturados
- **Redis:** Cache para respostas rápidas

### Serviços de Nuvem

- **AWS / Google Cloud / Azure:** Hospedagem e processamento
- **N8N:** Automação de workflows e integrações

### Ferramentas de Desenvolvimento

- **Iovable:** Plataforma para desenvolvimento da interface do totem
- **Git/GitHub:** Controle de versão
- **Docker:** Containerização (opcional)

### Segurança e Conformidade

- **Criptografia TLS 1.3:** Comunicação segura
- **OAuth 2.0:** Autenticação (se necessário)
- **Logs auditáveis:** Conformidade LGPD

---

## 🏗️ Arquitetura da Solução

### Visão Geral

A arquitetura do EDUBOT é dividida em camadas para garantir modularidade, escalabilidade e manutenibilidade.

```
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE INTERFACE                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Display    │  │  Microfone   │  │ Alto-falante │      │
│  │  Touchscreen │  │  (Voz)       │  │  (Áudio)     │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                  CAMADA DE PROCESSAMENTO                     │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Hardware Embarcado (ESP32 / Raspberry Pi)           │   │
│  │  - Reconhecimento de voz                             │   │
│  │  - Detecção de QR Code                               │   │
│  │  - Controle de sensores                              │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE BACKEND                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  API REST (Python/FastAPI)                           │   │
│  │  - Processamento de requisições                      │   │
│  │  - Integração com IA                                 │   │
│  │  - Gerenciamento de dados                            │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE IA                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   OpenAI     │  │   Whisper    │  │   Google     │      │
│  │   GPT-4      │  │  (Speech-to- │  │     TTS      │      │
│  │              │  │    Text)     │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                  CAMADA DE DADOS                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Supabase (PostgreSQL) + Redis (Cache)               │   │
│  │  - Dados acadêmicos                                  │   │
│  │  - Métricas de uso                                   │   │
│  │  - Logs de auditoria                                 │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                 CAMADA DE ANALYTICS                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Dashboard Institucional                             │   │
│  │  - Visualização de métricas                          │   │
│  │  - Relatórios de uso                                 │   │
│  │  - Análise de satisfação                             │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Fluxo de Dados

1. **Entrada:** Estudante interage por voz ou toque
2. **Captura:** Hardware captura áudio/toque e envia para backend
3. **Processamento:** IA processa a requisição e gera resposta
4. **Armazenamento:** Dados são salvos (anonimizados) no banco
5. **Resposta:** Informação é apresentada ao estudante (áudio + visual)
6. **Analytics:** Métricas são processadas para dashboard institucional

### Diagramas Detalhados

Os diagramas de arquitetura completos estão disponíveis na pasta `docs/diagramas/`:

- `arquitetura-geral.png` - Visão geral do sistema
- `fluxo-dados.png` - Pipeline de processamento de dados
- `pipeline-ia.png` - Fluxo de processamento de IA

---

## 📊 Estratégia de Coleta de Dados

### Dados Coletados

| Categoria | Dados | Finalidade | Anonimização |
|-----------|-------|------------|--------------|
| **Interação** | Pergunta, resposta, timestamp | Melhoria da IA | ✅ Sim |
| **Uso** | Horário, duração, localização do totem | Analytics | ✅ Sim |
| **Satisfação** | Avaliação (1-5 estrelas), feedback | Qualidade | ✅ Sim |
| **Técnicos** | Erros, latência, disponibilidade | Monitoramento | ✅ Sim |

### Métodos de Coleta

1. **Automática:** Registro de cada interação com timestamp
2. **Sensores:** Detecção de presença e tempo de uso
3. **Feedback Ativo:** Solicitação de avaliação após interação
4. **Logs de Sistema:** Erros, performance e disponibilidade

### Armazenamento

- **Banco de Dados:** Supabase (PostgreSQL) com criptografia
- **Retenção:** Dados anonimizados mantidos por 12 meses
- **Backup:** Backup diário automático em nuvem
- **Acesso:** Restrito a administradores autorizados

### Conformidade LGPD

- ✅ **Minimização:** Apenas dados essenciais são coletados
- ✅ **Anonimização:** Dados pessoais são anonimizados
- ✅ **Consentimento:** Aviso de coleta exibido no primeiro uso
- ✅ **Transparência:** Política de privacidade acessível
- ✅ **Segurança:** Criptografia e controle de acesso

---

## 🔒 Segurança e Privacidade

### Princípios de Segurança

1. **Privacy by Design:** Privacidade desde a concepção
2. **Minimização de Dados:** Coletar apenas o necessário
3. **Criptografia:** Dados em trânsito e em repouso
4. **Controle de Acesso:** Autenticação e autorização rigorosas
5. **Auditoria:** Logs de todas as operações sensíveis

### Medidas de Segurança

| Camada | Medida | Tecnologia |
|--------|--------|------------|
| **Comunicação** | Criptografia TLS 1.3 | HTTPS |
| **Dados** | Criptografia AES-256 | PostgreSQL |
| **Acesso** | Autenticação multifator | OAuth 2.0 |
| **Monitoramento** | Logs auditáveis | CloudWatch |
| **Backup** | Backup criptografado | AWS S3 |

### Conformidade LGPD

O EDUBOT está em conformidade com a Lei Geral de Proteção de Dados (Lei 13.709/2018):

- **Base Legal:** Legítimo interesse (melhoria de serviços educacionais)
- **Direitos do Titular:** Acesso, correção, exclusão de dados
- **DPO:** Encarregado de proteção de dados designado
- **Relatório de Impacto:** RIPD elaborado antes da implementação
- **Incidentes:** Procedimento de notificação em até 72h

---

## ♿ Acessibilidade Universal

O EDUBOT foi projetado para atender aos requisitos da **Lei Brasileira de Inclusão (Lei 13.146/2015)** e das **Diretrizes de Acessibilidade para Conteúdo Web (WCAG 2.1 - Nível AA)**.

### Acessibilidade para Deficiência Visual

- **Leitura de tela:** Todo conteúdo é lido em voz alta
- **Alto contraste:** Opção de cores contrastantes
- **Ampliação de texto:** Fontes ajustáveis (16px a 48px)
- **Navegação por voz:** Comandos falados para navegação
- **Botões em Braille:** Identificação tátil dos controles

### Acessibilidade para Deficiência Auditiva

- **Legendas:** Todo áudio possui legenda em texto
- **Tradução em Libras:** Integração futura com VLibras ou Hand Talk
- **Alertas visuais:** Notificações por meio de ícones e cores
- **Controle de volume:** Ajuste individual de volume

### Acessibilidade para Deficiência Cognitiva

- **Linguagem simples:** Frases curtas e diretas
- **Navegação intuitiva:** Interface minimalista
- **Tempo ajustável:** Sem limite de tempo para interação
- **Confirmações visuais:** Feedback claro de cada ação
- **Ajuda contextual:** Instruções em cada tela

### Acessibilidade para Deficiência Motora

- **Comandos por voz:** Interação sem necessidade de toque
- **Botões grandes:** Alvos de toque de no mínimo 44x44px
- **Espaçamento:** Distância mínima de 8px entre elementos
- **Altura ajustável:** Totem acessível para cadeirantes

### Acessibilidade para Baixo Letramento

- **Ícones universais:** Símbolos reconhecíveis
- **Áudio explicativo:** Todas as opções lidas em voz alta
- **Navegação guiada:** Passo a passo com instruções
- **Linguagem acessível:** Vocabulário simples e direto

---

## 📅 Plano de Desenvolvimento

### Cronograma Geral

O desenvolvimento do EDUBOT está planejado para 6 meses, dividido em 6 sprints de 4 semanas cada.

> **Nota:** As datas das Sprints 2-6 são estimativas para fins de planejamento. As datas reais serão definidas pela FIAP conforme o andamento do Challenge.

### Sprint 1: Planejamento e Documentação (Atual - Outubro 2025)

**Status:** ✅ Em andamento

**Objetivos:**
- Documentar justificativa do problema
- Definir arquitetura da solução
- Especificar tecnologias
- Criar estratégia de coleta de dados
- Elaborar plano de desenvolvimento

**Entregas:**
- ✅ README.md completo
- ✅ Diagramas de arquitetura
- ✅ Documentação de acessibilidade
- ✅ Repositório GitHub configurado

**Prazo:** 31/10/2025, 23h59

---

### Sprint 2: Desenvolvimento do Backend (Estimativa: Novembro 2025)

**Objetivos:**
- Configurar ambiente de desenvolvimento
- Desenvolver API REST com FastAPI
- Integrar OpenAI GPT-4 para IA conversacional
- Implementar Whisper para reconhecimento de voz
- Configurar banco de dados Supabase
- Implementar autenticação e segurança básica

**Entregas:**
- API funcional com endpoints principais
- Integração com IA conversacional
- Sistema de reconhecimento de voz
- Banco de dados estruturado
- Testes unitários do backend

---

### Sprint 3: Desenvolvimento do Frontend (Estimativa: Dezembro 2025)

**Objetivos:**
- Desenvolver interface do totem usando Iovable
- Implementar design acessível (WCAG 2.1)
- Criar componentes de interação por voz
- Integrar frontend com backend
- Implementar recursos de acessibilidade visual

**Entregas:**
- Interface funcional e acessível
- Integração com API backend
- Sistema de navegação por voz
- Testes de usabilidade
- Documentação de interface

---

### Sprint 4: Integração de Hardware (Estimativa: Janeiro 2026)

**Objetivos:**
- Configurar ESP32 / hardware embarcado
- Integrar sensores de proximidade
- Configurar câmera para QR Code
- Testar microfone e alto-falantes
- Integrar hardware com software

**Entregas:**
- Hardware funcional e integrado
- Sistema de detecção de presença
- Reconhecimento de QR Code
- Testes de integração hardware-software
- Documentação técnica de hardware

---

### Sprint 5: Acessibilidade e Integrações (Estimativa: Fevereiro 2026)

**Objetivos:**
- Implementar recursos avançados de acessibilidade
- Integrar VLibras ou Hand Talk (Libras)
- Desenvolver dashboard institucional
- Implementar sistema de analytics
- Realizar testes com usuários PcD

**Entregas:**
- Recursos de acessibilidade completos
- Dashboard funcional
- Sistema de métricas e analytics
- Relatório de testes com PcD
- Ajustes baseados em feedback

---

### Sprint 6: Testes, Ajustes e Lançamento (Estimativa: Março 2026)

**Objetivos:**
- Realizar testes de carga e performance
- Auditar segurança e conformidade LGPD
- Criar documentação de usuário
- Treinar equipe institucional
- Preparar lançamento piloto

**Entregas:**
- Sistema completo e testado
- Documentação completa (técnica e usuário)
- Relatório de auditoria de segurança
- Plano de implantação
- Lançamento piloto em instituição parceira

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

## 📱 Casos de Uso

### Caso de Uso 1: Consulta de Horário de Aula

**Ator:** Estudante

**Fluxo:**
1. Estudante se aproxima do totem
2. Totem ativa automaticamente (sensor de proximidade)
3. Estudante fala: *"Qual é o meu horário de aula hoje?"*
4. Sistema reconhece a voz e processa a pergunta
5. IA consulta banco de dados acadêmico
6. Totem exibe horário na tela e lê em voz alta
7. Estudante confirma: *"Obrigado"*
8. Sistema solicita avaliação (1-5 estrelas)
9. Estudante avalia e totem retorna ao estado inicial

**Benefício:** Acesso rápido à informação sem necessidade de login ou navegação complexa

---

### Caso de Uso 2: Estudante com Deficiência Visual

**Ator:** Estudante com deficiência visual

**Fluxo:**
1. Estudante se aproxima do totem
2. Totem detecta presença e anuncia: *"Olá! Como posso ajudar?"*
3. Estudante fala: *"Onde fica a biblioteca?"*
4. Sistema processa e responde em áudio: *"A biblioteca fica no 3º andar, bloco B. Deseja instruções detalhadas?"*
5. Estudante: *"Sim"*
6. Sistema fornece instruções passo a passo em áudio
7. Estudante agradece e se afasta
8. Totem retorna ao estado inicial

**Benefício:** Acessibilidade total sem necessidade de assistência humana

---

### Caso de Uso 3: Coleta de Feedback Institucional

**Ator:** Estudante

**Fluxo:**
1. Estudante interage com totem para consulta
2. Após resposta, totem pergunta: *"Como você avalia este atendimento?"*
3. Estudante seleciona 4 estrelas no touchscreen
4. Totem pergunta: *"Deseja deixar um comentário?"*
5. Estudante fala: *"O totem é muito útil, mas poderia ter mais informações sobre eventos"*
6. Sistema registra feedback (anonimizado)
7. Dashboard institucional recebe dados para análise
8. Instituição identifica demanda por informações de eventos

**Benefício:** Coleta estruturada de feedback para melhoria contínua

---

### Caso de Uso 4: Consulta em Horário de Pico

**Ator:** Múltiplos estudantes

**Fluxo:**
1. Fila de 5 estudantes aguardando atendimento
2. Primeiro estudante interage rapidamente (30 segundos)
3. Sistema processa e responde
4. Estudante se afasta, próximo se aproxima automaticamente
5. Processo se repete para todos os estudantes
6. Sistema registra horário de pico (12h-13h)
7. Dashboard mostra necessidade de totem adicional

**Benefício:** Redução de filas em secretarias e identificação de demandas

---

## 🏆 Diferenciais Competitivos

1. **Acessibilidade Total:** Conformidade completa com Lei 13.146/2015 e WCAG 2.1
2. **Interação por Voz:** Reconhecimento de voz como funcionalidade principal
3. **IA Conversacional:** Respostas inteligentes e contextualizadas
4. **Privacidade Garantida:** Conformidade total com LGPD
5. **Escalabilidade:** Solução replicável em milhares de instituições
6. **Analytics Institucional:** Dashboard com métricas valiosas
7. **Baixo Custo:** Uso de hardware acessível (ESP32) e APIs de IA

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
**Versão:** 2.0 (Simplificada)
