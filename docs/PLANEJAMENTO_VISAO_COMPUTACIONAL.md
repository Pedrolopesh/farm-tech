# Planejamento Técnico: Fase 6 - Visão Computacional FarmTech

## 1. Estrutura do Google Colab (Proposta)

### Bloco 1: Preparação do Ambiente e Dados
```python
# Instalação de dependências
!pip install ultralytics -q

# Importação de bibliotecas
import os
import torch
from ultralytics import YOLO
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import time

# Montagem do Drive (opcional para persistência)
# from google.colab import drive
# drive.mount('/content/drive')
```

### Bloco 2: Preparação de Dados (Modular)
- **CNN:** Organização em `train/` e `val/` (Já existente no repositório).
- **YOLO:** Criação do arquivo `farmtech.yaml`.
  ```yaml
  path: /content/dataset_yolo
  train: images/train
  val: images/val
  names:
    0: arco_iris
    1: trator
  ```

### Bloco 3: Treinamento - O Rigor dos Testes (30 vs 60 Épocas)
- **Experimento A:** CNN (30 épocas) vs CNN (60 épocas).
- **Experimento B:** YOLO Custom (30 épocas) vs YOLO Custom (60 épocas).

### Bloco 4: Avaliação e Comparação Crítica
- **Métricas:** mAP (YOLO), Acurácia (CNN).
- **Benchmarking:** Tempo médio de inferência em GPU/CPU.

---

## 2. Análise Crítica (Prévia)

### Por que YOLO vs CNN?
1. **Localização vs Classificação:** A CNN tradicional (`modelo_farmtech.h5`) classifica a imagem inteira. O YOLO detecta *onde* o objeto está (bounding boxes), sendo ideal para segurança patrimonial (ex: onde o trator está entrando).
2. **Tempo de Inferência:** O YOLO é otimizado para "You Only Look Once", processando a imagem em uma única passada, enquanto CNNs complexas podem exigir mais recursos dependendo da arquitetura.
3. **Escalabilidade:** Para a FarmTech, detectar múltiplos animais ou intrusos em um único frame exige a arquitetura de detecção do YOLO.

---

## 3. Próximos Passos na Documentação (README)
O relatório final deve seguir a estrutura acadêmica:
1. **Resumo Executivo**
2. **Metodologia de Coleta (80 imagens)**
3. **Análise de Convergência (Gráficos de Loss por Época)**
4. **Conclusão Técnica sobre Deploy (Edge vs Cloud)**
