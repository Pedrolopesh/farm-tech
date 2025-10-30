# 📐 Diagramas de Arquitetura - EDUBOT

Este documento descreve os diagramas de arquitetura do projeto EDUBOT.

---

## 📋 Lista de Diagramas

### 1. Arquitetura Geral do Sistema
**Arquivo:** `arquitetura-geral.png`

**Descrição:**  
Diagrama em camadas mostrando a arquitetura completa do EDUBOT, desde o hardware até a camada de segurança.

**Camadas:**
1. Apresentação (Display, Alto-falantes, Botões)
2. Interface (Frontend React)
3. Hardware/IoT (ESP32, Sensores, Raspberry Pi)
4. Aplicação (Backend FastAPI)
5. Inteligência Artificial (OpenAI, Whisper, TTS)
6. Dados (Supabase, Redis, S3)
7. Integração (WhatsApp, N8N)
8. Segurança (TLS, OAuth, LGPD)

---

### 2. Fluxo de Dados
**Arquivo:** `fluxo-dados.png`

**Descrição:**  
Pipeline detalhado mostrando como os dados fluem através do sistema, desde a coleta até a visualização.

**Etapas:**
1. **Coleta:** Interface → Frontend → Validação → Backend
2. **Processamento:** Autenticação → Cache → IA → Banco de Dados
3. **Análise:** Agregação → Métricas → Dashboard
4. **Armazenamento:** PostgreSQL → Backup S3 → Retenção LGPD
5. **Visualização:** Dashboard Admin → Relatórios → Exportação

---

### 3. Pipeline de Inteligência Artificial
**Arquivo:** `pipeline-ia.png`

**Descrição:**  
Fluxo específico de como a IA processa consultas dos usuários.

**Etapas:**
1. **Input:** Texto ou voz do usuário
2. **Pré-processamento:** Tokenização, lematização (spaCy)
3. **Classificação:** Identificação de intenção
4. **Contexto:** Enriquecimento com dados do usuário e histórico
5. **IA:** Processamento com GPT-4
6. **Pós-processamento:** Formatação e adaptação
7. **Output:** Resposta em texto, áudio ou Libras

---

## 🛠️ Como Criar os Diagramas

### Ferramenta Recomendada: diagrams.net

1. Acesse: https://app.diagrams.net/
2. Clique em "Create New Diagram"
3. Escolha template "Blank Diagram"
4. Use os elementos da biblioteca à esquerda

### Elementos Sugeridos:

**Para Arquitetura Geral:**
- Retângulos para componentes
- Setas para fluxo de dados
- Cores diferentes para cada camada
- Ícones para hardware (ESP32, Raspberry Pi)

**Para Fluxo de Dados:**
- Formas de processo (retângulos arredondados)
- Decisões (losangos)
- Armazenamento (cilindros)
- Setas direcionais

**Para Pipeline de IA:**
- Sequência linear
- Blocos de processamento
- Indicadores de entrada/saída

---

## 📏 Especificações Técnicas

**Formato:** PNG  
**Resolução:** Mínimo 1920x1080px  
**Tamanho:** Máximo 2MB por arquivo  
**Cores:** Usar paleta consistente (azul, verde, laranja)  
**Fonte:** Arial ou similar, tamanho mínimo 12pt  
**Legibilidade:** Garantir que texto seja legível mesmo em tamanhos menores

---

## ✅ Checklist de Qualidade

Antes de finalizar os diagramas, verifique:

- [ ] Todos os componentes estão rotulados
- [ ] Setas indicam direção do fluxo
- [ ] Cores são consistentes
- [ ] Texto é legível
- [ ] Não há elementos sobrepostos
- [ ] Legenda está incluída (se necessário)
- [ ] Arquivo está em alta resolução
- [ ] Nome do arquivo é descritivo

---

## 📝 Descrições para o README

Ao referenciar os diagramas no README.md, use:

```markdown
### Arquitetura Geral

O EDUBOT segue uma arquitetura em 8 camadas, conforme ilustrado no diagrama abaixo:

![Arquitetura Geral](docs/diagramas/arquitetura-geral.png)

*Figura 1: Arquitetura em camadas do EDUBOT*
```

---

**Última atualização:** 28/10/2025
