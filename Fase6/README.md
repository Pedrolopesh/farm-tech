# FarmTech Solutions

## Integrantes
| Nome | RM |
| :--- | :--- |
| *Fabrício Mouzer Brito* | RM566777 |
| *Enzo Nunes Castanheira Gloria da Silva* | RM567599 |
| *Larissa Nunes Moreira Reis* | RM568280 |
| *Gabriel Rapozo Guimarães Soares* | RM568480 |

## Introdução
A **FarmTech Solutions** apresenta uma solução inovadora de monitoramento agrícola baseada em Visão Computacional. O objetivo principal deste projeto é realizar a detecção, classificação e monitoramento de vacas e tratores em campo utilizando modelos de aprendizado profundo (Deep Learning). Através da inteligência artificial, buscamos otimizar o manejo animal, o monitoramento de maquinário agrícola e aumentar tanto a segurança quanto a produtividade das operações da fazenda.

## Notebook do Projeto
Acesse o notebook principal contendo o treinamento, avaliação e inferência dos modelos:
[EnzoGloria_rm567599_pbl_fase6.ipynb](./EnzoGloria_rm567599_pbl_fase6.ipynb)

## Comparação Técnica (Entregável 2)

Durante o desenvolvimento da solução, testamos diferentes abordagens. Abaixo está a tabela comparativa entre o YOLOv5 (treinado por 30 e 60 épocas) e a nossa CNN Customizada:

| Modelo / Abordagem | Facilidade de Uso | Precisão (Acurácia/mAP) | Tempo de Treinamento | Tempo de Inferência |
| :--- | :--- | :--- | :--- | :--- |
| **YOLOv5 (30 Épocas)** | Alta (Framework estruturado pronto para uso) | Boa (Rápida convergência inicial na detecção) | Rápido | Muito Rápido (Tempo Real) |
| **YOLOv5 (60 Épocas)** | Alta (Framework estruturado pronto para uso) | Muito Alta (Excelente ajuste aos dados e melhor detecção) | Moderado | Muito Rápido (Tempo Real) |
| **CNN Customizada** | Média (Exige design e codificação da arquitetura do zero) | Moderada (Alta dependência da sintonia fina de parâmetros) | Longo (Dependente da capacidade computacional) | Lento (Necessita otimizações para tempo real) |

## Instruções

Para visualizar e executar o notebook do projeto no Google Colab, siga os passos abaixo:

1. Acesse o [Google Colab](https://colab.research.google.com/).
2. No menu principal, clique em **Arquivo > Fazer upload de notebook**.
3. Selecione a aba **GitHub** e cole o link para o repositório/arquivo, ou faça o upload direto do arquivo `EnzoGloria_rm567599_pbl_fase6.ipynb` a partir da sua máquina.
4. Para garantir um treinamento rápido, certifique-se de usar o acelerador de hardware. Vá em **Ambiente de execução > Alterar o tipo de ambiente de execução** e selecione **T4 GPU** (ou outra GPU disponível).
5. Execute as células de cima para baixo.

## Conclusão
O **YOLOv5** foi a escolha principal para a solução da FarmTech. Isso se deve à sua excepcional facilidade de uso, alta precisão mesmo com um número reduzido de épocas (com resultados ótimos em 60 épocas) e sua maior vantagem: a velocidade de inferência. Como a FarmTech precisa monitorar vacas e tratores em campo, a capacidade de rodar as detecções em tempo real (Real-Time) é essencial. Enquanto a CNN customizada exigiu um tempo considerável para o design arquitetural e calibração, o YOLOv5 nos entregou um pipeline robusto, escalável e perfeitamente alinhado com as exigências do monitoramento de precisão.