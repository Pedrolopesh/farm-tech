# 📤 Guia de Submissão - Challenge FlexMedia

**Aluno:** Fabrício Mouzer Brito  
**RM:** 566777  
**Prazo:** 31/10/2025, 23h59

---

## 🎯 Objetivo

Este guia te orienta passo a passo para submeter o projeto EDUBOT no GitHub e no portal FIAP.

---

## ✅ Checklist Pré-Submissão

Antes de começar, verifique se você tem:

- [ ] Conta no GitHub (se não tiver, crie em https://github.com/signup)
- [ ] Todos os arquivos do projeto baixados
- [ ] Acesso ao portal FIAP
- [ ] Dados da tutora: Ana Cristana dos Santos (@anacrissantos)

---

## 📋 Passo a Passo Completo

### PARTE 1: Criar Repositório no GitHub

#### Passo 1: Acessar GitHub

1. Abra seu navegador
2. Acesse: https://github.com
3. Faça login com sua conta

#### Passo 2: Criar Novo Repositório

1. No canto superior direito, clique no ícone **"+"**
2. Selecione **"New repository"**

#### Passo 3: Configurar Repositório

Preencha os campos:

**Repository name:**
```
edubot-totem-inteligente
```

**Description:**
```
Challenge FlexMedia - Totem Inteligente Acessível para Ambientes Educacionais com IA
```

**Visibilidade:**
- ⚠️ **Selecione: PRIVATE** (muito importante!)

**Initialize repository:**
- ✅ Marque: "Add a README file"
- ⚠️ NÃO marque: ".gitignore" (já temos um)
- ⚠️ NÃO marque: "Choose a license"

#### Passo 4: Criar Repositório

1. Clique no botão verde **"Create repository"**
2. Aguarde a criação (alguns segundos)

---

### PARTE 2: Adicionar Tutora como Colaboradora

#### Passo 5: Acessar Configurações

1. No repositório recém-criado, clique em **"Settings"** (menu superior)
2. No menu lateral esquerdo, clique em **"Collaborators"** ou **"Manage Access"**

#### Passo 6: Adicionar Colaboradora

1. Clique no botão **"Add people"** ou **"Invite a collaborator"**
2. Digite: `anacrissantos`
3. Quando aparecer o perfil de **Ana Cristana dos Santos**, clique nele
4. Clique em **"Add anacrissantos to this repository"**
5. Confirme o convite

⚠️ **Importante:** A tutora tem 7 dias para aceitar o convite. Ela estará atenta para aceitar rapidamente.

---

### PARTE 3: Fazer Upload dos Arquivos

#### Passo 7: Voltar para o Repositório

1. Clique no nome do repositório no topo da página
2. Você verá a página principal com o README padrão

#### Passo 8: Fazer Upload dos Arquivos

**Opção A: Via Interface Web (Mais Fácil)**

1. Clique em **"Add file"** → **"Upload files"**
2. Arraste todos os arquivos e pastas do projeto para a área indicada
3. Ou clique em **"choose your files"** e selecione os arquivos

**Estrutura a ser enviada:**
```
edubot-totem-inteligente/
├── README.md (substitua o existente)
├── .gitignore
├── GUIA_SUBMISSAO.md
├── docs/
│   ├── diagramas/
│   │   ├── DIAGRAMAS.md
│   │   ├── arquitetura-geral.png (você deve criar)
│   │   ├── fluxo-dados.png (você deve criar)
│   │   └── pipeline-ia.png (você deve criar)
│   ├── arquitetura/
│   ├── acessibilidade/
│   └── seguranca/
└── planejamento/
```

4. Na caixa **"Commit changes"**, escreva:
```
Adicionar documentação completa do projeto EDUBOT
```

5. Clique no botão verde **"Commit changes"**

**Opção B: Via Git (Linha de Comando)**

Se você tem Git instalado:

```bash
# Navegar até a pasta do projeto
cd /caminho/para/edubot-totem-inteligente

# Inicializar repositório local
git init

# Adicionar remote (substitua SEU_USUARIO pelo seu username GitHub)
git remote add origin https://github.com/SEU_USUARIO/edubot-totem-inteligente.git

# Adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Adicionar documentação completa do projeto EDUBOT"

# Enviar para GitHub
git branch -M main
git push -u origin main
```

---

### PARTE 4: Verificar Upload

#### Passo 9: Confirmar Arquivos

1. Volte para a página principal do repositório
2. Verifique se todos os arquivos e pastas estão visíveis
3. Clique no README.md e confirme que o conteúdo está correto
4. Navegue pelas pastas `docs/` e `planejamento/` para confirmar

---

### PARTE 5: Criar Diagramas de Arquitetura

⚠️ **Importante:** Você precisa criar os diagramas antes de submeter!

#### Passo 10: Acessar diagrams.net

1. Abra: https://app.diagrams.net/
2. Clique em **"Create New Diagram"**
3. Escolha **"Blank Diagram"**
4. Dê um nome: `arquitetura-geral`

#### Passo 11: Criar Diagrama de Arquitetura Geral

**Elementos a incluir:**

1. **Camada de Apresentação:**
   - Display Touchscreen
   - Alto-falantes
   - Botões Táteis

2. **Camada de Interface:**
   - React.js + TailwindCSS

3. **Camada de Hardware/IoT:**
   - ESP32-CAM
   - Sensor PIR
   - Raspberry Pi 4

4. **Camada de Aplicação:**
   - FastAPI (Python)

5. **Camada de IA:**
   - OpenAI GPT-4
   - Whisper
   - Google TTS

6. **Camada de Dados:**
   - Supabase (PostgreSQL)
   - Redis
   - AWS S3

7. **Camada de Integração:**
   - WhatsApp Business
   - N8N

8. **Camada de Segurança:**
   - TLS 1.3
   - OAuth 2.0
   - LGPD

**Dicas:**
- Use retângulos para componentes
- Use setas para mostrar fluxo
- Use cores diferentes para cada camada
- Adicione ícones (biblioteca à esquerda)

#### Passo 12: Salvar Diagrama

1. Clique em **"File"** → **"Export as"** → **"PNG"**
2. Configurações:
   - Zoom: 100%
   - Border Width: 10
   - Transparent Background: NÃO
3. Clique em **"Export"**
4. Salve como: `arquitetura-geral.png`

#### Passo 13: Repetir para Outros Diagramas

Crie também:
- `fluxo-dados.png` (pipeline de dados)
- `pipeline-ia.png` (fluxo de IA)

Consulte `docs/diagramas/DIAGRAMAS.md` para detalhes de cada diagrama.

#### Passo 14: Fazer Upload dos Diagramas

1. Volte ao repositório no GitHub
2. Navegue até `docs/diagramas/`
3. Clique em **"Add file"** → **"Upload files"**
4. Faça upload dos 3 arquivos PNG
5. Commit message: `Adicionar diagramas de arquitetura`
6. Clique em **"Commit changes"**

---

### PARTE 6: Revisão Final

#### Passo 15: Checklist de Qualidade

Verifique se o repositório contém:

- [ ] README.md completo e bem formatado
- [ ] .gitignore configurado
- [ ] Estrutura de pastas organizada
- [ ] 3 diagramas de arquitetura (PNG)
- [ ] Documentação adicional em `docs/`
- [ ] Tutora adicionada como colaboradora
- [ ] Repositório está PRIVADO

#### Passo 16: Testar Visualização

1. Abra o README.md no GitHub
2. Leia do início ao fim
3. Verifique se as imagens dos diagramas estão carregando
4. Confira se não há erros de formatação

---

### PARTE 7: Copiar Link do Repositório

#### Passo 17: Obter URL

1. Na página principal do repositório, clique no botão verde **"Code"**
2. Copie a URL que aparece (algo como: `https://github.com/SEU_USUARIO/edubot-totem-inteligente`)
3. Cole em um bloco de notas para não perder

---

### PARTE 8: Submeter no Portal FIAP

#### Passo 18: Acessar Portal FIAP

1. Abra: https://on.fiap.com.br/ (ou o portal que você usa)
2. Faça login com suas credenciais
3. Navegue até a disciplina do Challenge

#### Passo 19: Localizar Atividade

1. Procure por **"Challenge FlexMedia"** ou **"Sprint 1"**
2. Clique na atividade

#### Passo 20: Submeter Link

1. Procure o campo para envio
2. Cole o link do repositório GitHub
3. Verifique se o link está correto
4. Adicione uma observação (opcional):
```
Repositório privado com documentação completa do projeto EDUBOT.
Tutora Ana Cristana dos Santos (@anacrissantos) foi adicionada como colaboradora.
```

#### Passo 21: Confirmar Submissão

1. Clique em **"Enviar"** ou **"Submeter"**
2. Aguarde confirmação
3. **IMPORTANTE:** Tire um print da tela de confirmação
4. Salve o print com nome: `confirmacao_submissao_edubot.png`

---

### PARTE 9: Confirmação e Backup

#### Passo 22: Enviar E-mail de Confirmação (Opcional mas Recomendado)

Envie um e-mail para sua tutora:

**Para:** [e-mail da tutora]  
**Assunto:** Challenge FlexMedia - Submissão Projeto EDUBOT - RM 566777  
**Corpo:**

```
Prezada Professora Ana Cristana,

Venho por meio deste e-mail confirmar a submissão do projeto EDUBOT 
(Totem Inteligente Acessível para Ambientes Educacionais) referente 
ao Challenge FlexMedia - Sprint 1.

Dados da Submissão:
- Aluno: Fabrício Mouzer Brito
- RM: 566777
- Turma: R
- Data de Submissão: [DATA]
- Hora de Submissão: [HORA]

Link do Repositório GitHub (privado):
https://github.com/SEU_USUARIO/edubot-totem-inteligente

A senhora foi adicionada como colaboradora no repositório e deve ter 
recebido um convite por e-mail do GitHub.

O repositório contém:
✅ README.md completo (1000+ linhas)
✅ Justificativa do problema
✅ Descrição da solução
✅ Tecnologias utilizadas
✅ Diagramas de arquitetura (3)
✅ Estratégia de coleta de dados
✅ Plano de desenvolvimento
✅ Documentação de acessibilidade
✅ Segurança e LGPD

Fico à disposição para qualquer esclarecimento.

Atenciosamente,
Fabrício Mouzer Brito
RM: 566777
E-mail: fabriciomouzer@hotmail.com
```

#### Passo 23: Fazer Backup Local

1. Baixe uma cópia de todos os arquivos do projeto
2. Salve em pelo menos 2 locais diferentes:
   - Seu computador
   - Google Drive / OneDrive / Dropbox
3. Nomeie a pasta: `EDUBOT_Backup_[DATA]`

---

## ⚠️ Problemas Comuns e Soluções

### Problema 1: Não consigo criar repositório privado

**Solução:**  
Repositórios privados são gratuitos no GitHub. Se não conseguir, verifique se está logado corretamente. Contas gratuitas têm acesso a repositórios privados ilimitados.

### Problema 2: Tutora não aparece ao buscar

**Solução:**  
Certifique-se de digitar exatamente: `anacrissantos` (sem espaços, tudo minúsculo). Se não aparecer, tente adicionar pelo e-mail da tutora.

### Problema 3: Upload de arquivos falha

**Solução:**  
- Verifique sua conexão com internet
- Tente fazer upload de poucos arquivos por vez
- Se persistir, use a opção de linha de comando (Git)

### Problema 4: Diagramas não aparecem no README

**Solução:**  
Verifique se:
- Os arquivos PNG estão na pasta correta (`docs/diagramas/`)
- Os nomes dos arquivos estão corretos (sem espaços, tudo minúsculo)
- O caminho no README está correto: `![Texto](docs/diagramas/arquivo.png)`

### Problema 5: Repositório não está privado

**Solução:**  
1. Vá em **Settings** do repositório
2. Role até o final da página
3. Na seção **Danger Zone**, clique em **"Change visibility"**
4. Selecione **"Make private"**
5. Confirme digitando o nome do repositório

---

## 📞 Contatos de Emergência

**Tutora:** Ana Cristana dos Santos  
**GitHub:** @anacrissantos

**Aluno:** Fabrício Mouzer Brito  
**E-mail:** fabriciomouzer@hotmail.com  
**RM:** 566777

**Suporte FIAP:** [inserir contato se disponível]

---

## ✅ Checklist Final

Antes de considerar a submissão completa, confirme:

- [ ] Repositório GitHub criado e PRIVADO
- [ ] Tutora adicionada como colaboradora
- [ ] Todos os arquivos enviados
- [ ] 3 diagramas de arquitetura criados e enviados
- [ ] README.md completo e bem formatado
- [ ] Link do repositório submetido no portal FIAP
- [ ] Print de confirmação salvo
- [ ] E-mail de confirmação enviado (opcional)
- [ ] Backup local realizado
- [ ] Prazo respeitado (31/10/2025, 23h59)

---

## 🎉 Parabéns!

Se você completou todos os passos, seu projeto está submetido com sucesso! 

Agora é só aguardar o feedback da tutora e se preparar para as próximas sprints.

**Boa sorte! 🚀**

---

**Última atualização:** 28/10/2025  
**Versão:** 1.0
