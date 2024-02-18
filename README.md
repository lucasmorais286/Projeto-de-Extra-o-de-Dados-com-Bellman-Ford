Projeto Algoritmo de Bellman-Ford para Rotas em Roma
Este projeto utiliza o algoritmo de Bellman-Ford para encontrar o melhor caminho entre duas esquinas em Roma, com base em uma tabela que descreve as conexões entre as ruas e estradas. A base de dados foi obtida do site da universidade de Roma, e está disponível ao público no link http://www.diag.uniroma1.it/challenge9/download.shtml. A base de dados contem informação de uma grande parcela das ruas/estradas de roma. Seus 3353 vértices representam esquinas e suas 8870 arestas representam ruas, estradas ou recortes destas. O grafo é conexo, não direcionado e possui pesos representando o comprimento das arestas em metros de maneira aproximada.  

Requisitos:
Python 3 e
Pandas

Como Usar:
Clone este repositório.
Execute bellman_ford_roma.py e insira o índice do vértice de origem e destino. Se preferir uma saída de caminho mais curto no formato de uma lista de arestas, insira 'lista' como terceira entrada. Se preferir um texto mais amigável a leitura, insira 'texto'.
O código calculará o melhor caminho e exibirá a distância total.
