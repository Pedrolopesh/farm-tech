import cv2
import os
import random
import shutil

def preparar_dados():
    origem = 'dataset'
    destino_base = 'dataset_final'
    tamanho = (224, 224)
    split_ratio = 0.8 # 80% para treino, 20% para validação

    for classe in ['vaca', 'tratores']:
        caminho_classe = os.path.join(origem, classe)
        arquivos = [f for f in os.listdir(caminho_classe) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        # Embaralha para a divisão ser justa
        random.shuffle(arquivos)
        
        limite = int(len(arquivos) * split_ratio)
        treino_files = arquivos[:limite]
        val_files = arquivos[limite:]

        for tipo, lista_arquivos in [('train', treino_files), ('val', val_files)]:
            pasta_destino = os.path.join(destino_base, tipo, classe)
            os.makedirs(pasta_destino, exist_ok=True)
            
            print(f"Processando {tipo} - {classe} ({len(lista_arquivos)} imagens)...")
            
            for nome_arq in lista_arquivos:
                try:
                    img = cv2.imread(os.path.join(caminho_classe, nome_arq))
                    if img is not None:
                        img_res = cv2.resize(img, tamanho)
                        cv2.imwrite(os.path.join(pasta_destino, nome_arq), img_res)
                except:
                    continue

    print("\n✅ Dataset pronto em 'dataset_final'!")
    print("Estrutura criada: train/ (para estudo) e val/ (para testes).")

if __name__ == "__main__":
    preparar_dados()