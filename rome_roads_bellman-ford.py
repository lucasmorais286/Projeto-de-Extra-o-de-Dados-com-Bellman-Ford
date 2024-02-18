import pandas as pd
from grafo import Grafo

# Recebe base de dados em csv e inicializa o grafo com o devido número de vértices, obtidos na informação da base de dados. 
base_dados = pd.read_csv('rome_roads.csv')
num_vertices = 3353
grafo = Grafo(num_vertices)

# Percorre a base de dados procurando as entradas de origem, destino e peso, então inicializa as arestas.
for linha, informacao_atual in base_dados.iterrows():
    origem = informacao_atual['Origem']
    destino = informacao_atual['Destino'] 
    peso = informacao_atual['Peso']
    grafo.add_aresta(origem,destino,peso)
print('O grafo inicializado representa a organização de ruas e estradas da cidade de Roma. Vértices representam esquinas selecionadas e arestas representam os caminhos que as conectam. Os pesos são representações das distâncias aproximadas em metros. Os vértices são identificados por números naturais, partindo do 1 até o 3353.')
origem_busca = int(input('Insira o índice do vértice de origem(entre 1 e 3353) para a busca do menor caminho: '))
destino_busca = int(input('Insira o índice vértice de destino(entre 1 e 3353) para a busca do menor caminho: '))
preferencia = input('Insira "lista" se prefere receber o caminho como uma lista de arestas ou "texto" caso você prefira receber o caminho especificado em forma de texto: ')
grafo.bellman_ford(origem_busca,destino_busca,preferencia)
