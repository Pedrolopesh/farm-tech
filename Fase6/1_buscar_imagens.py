import os
from icrawler.builtin import BingImageCrawler

def coletar():
    # Definimos 60 para garantir que, após a limpeza, tenhamos as 40+ exigidas
    quantidade = 60
    categorias = {
        'arco_iris': 'rainbow in the sky',
        'tratores': 'farm tractor machine'
    }
    
    for pasta, termo in categorias.items():
        caminho = os.path.join('dataset', pasta)
        if not os.path.exists(caminho):
            os.makedirs(caminho)
        
        print(f"\n--- Iniciando download de: {termo} ---")
        crawler = BingImageCrawler(storage={'root_dir': caminho})
        crawler.crawl(keyword=termo, max_num=quantidade)

if __name__ == "__main__":
    coletar()
    