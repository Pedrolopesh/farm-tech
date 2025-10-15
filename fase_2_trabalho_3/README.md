Link do repositório: 

# 🧾 Sistema de Gestão Financeira do Produtor Rural  
### (Cana-de-Açúcar, Soja e Açaí)

---

## 🌱 Contexto do Agronegócio

O **agronegócio** é um dos setores mais importantes da economia brasileira, sendo responsável por uma grande parcela do PIB, geração de empregos e fornecimento de alimentos e matérias-primas.  
Dentro desse universo, a **gestão financeira** é um dos maiores desafios do produtor rural, especialmente em propriedades que cultivam múltiplas culturas — como **Cana-de-Açúcar**, **Soja** e **Açaí**.

Muitos produtores enfrentam dificuldades para **registrar receitas e despesas**, **acompanhar margens de lucro por cultura** e **ter clareza sobre a saúde financeira do negócio**.  
Pensando nisso, este projeto propõe uma solução simples, clara e funcional que ataca diretamente essa dor do setor.

---

## 🎯 Objetivo da Solução

Desenvolver um **sistema de gestão financeira via prompt de comando**, que:
- Permita **cadastrar, consultar, corrigir e excluir transações financeiras** de receitas e despesas;
- Faça o **controle segmentado por cultura agrícola** (Cana, Soja, Açaí);
- Gere **relatórios e resumos automáticos por cultura**, exibindo a margem financeira de cada uma;
- Armazene os dados **em memória, arquivos (CSV/JSON)** e também **em banco de dados Oracle**;
- Assegure a **consistência e validação dos dados** de entrada (para evitar erros de digitação ou formato);
- Mantenha uma **usabilidade limpa e intuitiva**, mesmo sendo via terminal.

---

## 🧠 Conceitos de Python aplicados (Capítulos 3 a 6)

| Conteúdo solicitado | Implementação prática |
|----------------------|-----------------------|
| **Subalgoritmos (funções e procedimentos)** | O sistema foi estruturado em dezenas de funções independentes, como `criar_transacao()`, `corrigir_transacao()`, `exportar_csv()`, `resumo_por_cultura()`, todas com passagem de parâmetros e responsabilidades bem definidas. |
| **Estruturas de dados** | Uso de **listas e dicionários** para armazenar transações (`transacoes: List[Dict]`). Cada transação representa um registro completo do fluxo financeiro. |
| **Manipulação de arquivos** | Implementadas funções de exportação em **CSV (`exportar_csv`)** e **JSON (`exportar_json`)**, com estrutura organizada e cabeçalhos padronizados. |
| **Conexão com banco de dados (Oracle)** | Integração completa via **`oracledb`**, com cursores para **inserção, alteração, exclusão e consulta**. O sistema grava e mantém sincronizados os dados entre a lista em memória e a tabela Oracle. |

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.10+**
- **Oracle Database (FIAP Cloud)** via `oracledb`
- **Bibliotecas:** `csv`, `json`, `decimal`, `datetime`, `pandas`, `pathlib`
- **Interface:** linha de comando (CLI)
- **Arquivos gerados:**  
  - `export/transacoes.csv`  
  - `export/transacoes.json`

---

## 💡 Estrutura Lógica da Solução

1. **Menu principal** (interface de interação via prompt)
   - [1] Cadastrar transação  
   - [2] Listar transações (com filtro por cultura)  
   - [3] Corrigir (editar) transação  
   - [4] Remover transação  
   - [5] Resumo por cultura  
   - [6] Exportar CSV  
   - [7] Exportar JSON  
   - [8] Carregar dados de exemplo (seeds)  
   - [9] Listar transações gravadas no Oracle  

2. **Fluxo do sistema**
   - **Cadastro:** o usuário insere informações validadas de uma transação (receita ou despesa).  
     → Armazena na **lista em memória** e grava no **Oracle**.  
   - **Listagem:** exibe dados limpos e alinhados, com opção de filtrar por cultura.  
   - **Correção:** permite editar campos específicos, recalculando automaticamente os valores.  
     → Atualiza tanto na memória quanto no Oracle (`UPDATE`).  
   - **Remoção:** exclui o item selecionado e reflete no Oracle (`DELETE`).  
   - **Resumo:** apresenta a **margem financeira** (receita - despesa) de cada cultura.  
   - **Exportação:** gera os arquivos CSV e JSON de backup local.  

---

## 🌾 Inovação e Relevância

- **Inovação prática:** o sistema oferece **resumo automático por cultura**, ajudando o produtor a identificar **quais lavouras geram mais lucro ou prejuízo**.
- **Integração completa:** sincroniza dados entre memória, arquivos e banco Oracle.
- **Usabilidade aprimorada:** menus numerados, validação de entradas, mensagens de sucesso/erro claras e feedback visual.
- **Segurança de dados:** uso de `Decimal` para cálculos financeiros, evitando erros de arredondamento de ponto flutuante.
- **Escalabilidade:** pode ser facilmente adaptado para outros tipos de cultura ou categorias de despesa.

---

## 🔍 Exemplo de Estrutura de Dados

Cada transação é representada por um dicionário Python, como o exemplo abaixo:

```json
{
  "id": 1,
  "tipo": "Receita",
  "data": "2025-10-15",
  "cultura": "Soja",
  "categoria": "Venda (grão/fruto)",
  "descricao": "Venda de soja a granel",
  "quantidade": "50.000",
  "unidade": "sc",
  "preco_unitario": "160.00",
  "total": "8000.00",
  "valor_assinado": "8000.00",
  "metodo_pagamento": "Pix",
  "contraparte": "Cooperativa X",
  "observacoes": null,
  "created_at": "2025-10-15"
}
```

```
CREATE TABLE TRANSACOES (
  ID              NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  TIPO            VARCHAR2(20),
  DATA            DATE,
  CULTURA         VARCHAR2(50),
  CATEGORIA       VARCHAR2(50),
  DESCRICAO       VARCHAR2(200),
  QUANTIDADE      NUMBER(15,3),
  UNIDADE         VARCHAR2(10),
  PRECO_UNITARIO  NUMBER(15,2),
  TOTAL           NUMBER(15,2),
  VALOR_ASSINADO  NUMBER(15,2),
  METODO_PAGAMENTO VARCHAR2(30),
  CONTRAPARTE     VARCHAR2(100),
  OBSERVACOES     VARCHAR2(255),
  CREATED_AT      DATE DEFAULT SYSDATE
);
```


O sistema executa **instruções SQL completas**:
- `INSERT INTO TRANSACOES (...) VALUES (...)`  
- `UPDATE TRANSACOES SET ... WHERE ID = :id`  
- `DELETE FROM TRANSACOES WHERE ID = :id`  
- `SELECT * FROM TRANSACOES ORDER BY ID DESC`

---

## 🧮 Validações e Consistência de Dados

O sistema garante integridade e evita entradas incorretas:
- Tipos de transação: apenas `"Receita"` ou `"Despesa"`;
- Culturas: `"Cana-de-açúcar"`, `"Soja"`, `"Açaí"`;
- Categorias, métodos de pagamento e unidades são pré-definidos via listas;
- Campos numéricos (quantidade, preço, total) usam `Decimal` para evitar imprecisões;
- Datas exigem formato `DD/MM/AAAA` e são convertidas para `date`;
- Confirmadores (`s/n`) em ações destrutivas (remoção e correção).

---

## 💾 Exportação de Dados

- **CSV:** gera um arquivo tabular fácil de importar em Excel ou Power BI.  
- **JSON:** ideal para integração com outros sistemas ou APIs futuras.  

Local de exportação:
- `/export/transacoes.csv`
- `/export/transacoes.json`

---

## 🧭 Execução do Programa

### 1. Pré-requisitos
- Python 3.10+ instalado  
- Bibliotecas: `oracledb`, `pandas`  

### 2. Execução
```bash
python3 main.py
```

### 3. Exemplo de uso

```
=== Menu ===
[1] Cadastrar transação
[2] Listar transações
[3] Corrigir (editar) transação
[4] Remover transação
[5] Resumo por cultura
[6] Exportar CSV
[7] Exportar JSON
[8] Carregar seeds de exemplo
[9] Listar transações do Oracle
[0] Sair

```

#### 📊 Resultado Esperado (Resumo por Cultura)

```
Cultura              | Receita (R$) | Despesa (R$) | Margem (R$)
---------------------+--------------+--------------+-------------
Cana-de-açúcar       |       0.00   |    -700.00   |    -700.00
Soja                 |    8000.00   |       0.00   |    8000.00
Açaí                 |       0.00   |    -450.00   |    -450.00
Sem vínculo          |       0.00   |       0.00   |       0.00
```

### Fluxo do Sistema

```
┌───────────────────┐
│       Usuário     │
└───────┬───────────┘
        │
        ▼
┌───────────────────────────────┐
│ Interface via Prompt (Menu)   │
└───────────┬───────────────────┘
            │
            ▼
┌───────────────────────────────┐
│ Lista em Memória (transações) │
└───────────┬───────────────────┘
            │
     ┌──────┼──────────┐
     ▼                 ▼
┌─────────────┐   ┌─────────────┐
│ CSV / JSON  │   │ Banco Oracle│
│ (Exportação)│   │ (Persistência)│
└─────────────┘   └─────────────┘

```

## 🧩 Conclusão

O sistema cumpre todos os **requisitos pedagógicos e técnicos** da atividade:

✅ Linha lógica clara e objetiva  
✅ Clareza sobre o que é tratado do agronegócio  
✅ Relevância prática e aderência ao tema  
✅ Inovação aplicada (resumo automatizado e integração total)  
✅ Consistência e validação das entradas  
✅ Boa usabilidade e apresentação limpa via prompt  
✅ Uso comprovado dos conceitos: **funções, estruturas, arquivos e Oracle**

---

## 👥 Integrantes

**PEDRO HENRIQUE LOPES DOS SANTOS**
RM: **RM568359**

**LARISSA NUNES MOREIRA REIS**
RM: **RM568280**

**ENZO NUNES CASTANHEIRA GLORIA DA SILVA**
RM: **RM567599**

**FABRICIO MOUZER BRITO**
RM: **RM566777**

**GABRIEL RAPOZO GUIMARÃES SOARES**
RM: **RM568480**
---

## 🏁 Créditos e Informações Finais

Projeto desenvolvido como parte da disciplina **Python para o Agronegócio**, do curso de **Técnologo em Inteligência Artificial (FIAP)**.  

Este trabalho aborda uma dor real do setor agro: a **gestão financeira multiculura**.  
A proposta une **simplicidade de uso**, **robustez técnica** e **integração com banco Oracle**, representando uma aplicação prática e moderna dos conteúdos estudados.

---

## 🏷️ Badges e Identificação

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Oracle](https://img.shields.io/badge/Oracle-Database-red?logo=oracle)
![FIAP](https://img.shields.io/badge/FIAP-ADS%20%7C%20Agroneg%C3%B3cio-cc0044?logo=fiap&logoColor=white)
![Status](https://img.shields.io/badge/Projeto-Finalizado-success?style=flat)

---

> 🌾 **"A tecnologia é o novo solo fértil do campo."**  
> Este projeto mostra como o **Python pode gerar valor real** para o produtor rural brasileiro.
