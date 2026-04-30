import os
import shutil
import random

def organizar_dataset():
    # Caminhos base
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_dir = os.path.join(base_dir, 'dataset')
    final_dir = os.path.join(base_dir, 'dataset_final')
    
    # Classes e seus respectivos IDs
    classes = {
        'vaca': {'id': 0, 'folder': 'vaca'},
        'trator': {'id': 1, 'folder': 'tratores'}
    }
    
    # Proporções de divisão
    splits = {'train': 0.8, 'val': 0.1, 'test': 0.1}
    
    # Criar a nova estrutura de diretórios
    print("Criando estrutura de diretórios em dataset_final...")
    for split in splits.keys():
        os.makedirs(os.path.join(final_dir, split, 'images'), exist_ok=True)
        os.makedirs(os.path.join(final_dir, split, 'labels'), exist_ok=True)

    for class_name, info in classes.items():
        class_id = info['id']
        src_folder = os.path.join(dataset_dir, info['folder'])
        
        if not os.path.exists(src_folder):
            print(f"Aviso: A pasta {src_folder} não foi encontrada. Ignorando...")
            continue
            
        print(f"Processando a classe '{class_name}' (ID {class_id})...")
        
        # Coletar todas as imagens
        images = [f for f in os.listdir(src_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        # Ordenar e embaralhar com seed fixa para reprodutibilidade, ou totalmente aleatório
        images.sort()
        random.seed(42)
        random.shuffle(images)
        
        total = len(images)
        train_end = int(total * splits['train'])
        val_end = train_end + int(total * splits['val'])
        
        split_data = {
            'train': images[:train_end],
            'val': images[train_end:val_end],
            'test': images[val_end:]
        }
        
        for split_name, imgs in split_data.items():
            for img_name in imgs:
                # Copiar imagem
                src_img_path = os.path.join(src_folder, img_name)
                dest_img_path = os.path.join(final_dir, split_name, 'images', img_name)
                shutil.copy(src_img_path, dest_img_path)
                
                # Processar e copiar label
                txt_name = os.path.splitext(img_name)[0] + '.txt'
                src_txt_path = os.path.join(src_folder, txt_name)
                dest_txt_path = os.path.join(final_dir, split_name, 'labels', txt_name)
                
                if os.path.exists(src_txt_path):
                    with open(src_txt_path, 'r') as f_in, open(dest_txt_path, 'w') as f_out:
                        for line in f_in:
                            parts = line.strip().split()
                            if parts:
                                # Garantir o mapeamento correto do ID da classe
                                parts[0] = str(class_id)
                                f_out.write(' '.join(parts) + '\n')
                else:
                    # Se não houver arquivo .txt (imagem sem bounding box), podemos criar um vazio
                    # ou apenas ignorar (o YOLO aceita imagens sem .txt correspondente como background)
                    pass

    # Gerar o arquivo dataset.yaml
    print("Gerando arquivo dataset.yaml...")
    yaml_path = os.path.join(base_dir, 'dataset.yaml')
    yaml_content = """path: /content/dataset_final
train: train/images
val: val/images
test: test/images

nc: 2
names: ['vaca', 'trator']
"""
    # Nota: No script estou utilizando 'train/images' em vez de 'images/train' 
    # para que o caminho reflita exatamente a estrutura de pastas solicitada:
    # "contendo as subpastas train, val e test. Dentro de cada uma, deve haver as pastas images e labels."
    
    with open(yaml_path, 'w') as f:
        f.write(yaml_content)
        
    print(f"\nSucesso! Estrutura criada em: {final_dir}")
    print(f"Arquivo YAML criado em: {yaml_path}")
    print("O dataset está pronto para ser zipado e enviado ao Google Drive para o treinamento.")

if __name__ == "__main__":
    organizar_dataset()
