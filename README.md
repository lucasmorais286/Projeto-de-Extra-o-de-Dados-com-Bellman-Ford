Projeto Algoritmo de Bellman-Ford para Rotas em Roma
Este projeto utiliza o algoritmo de Bellman-Ford para encontrar o melhor caminho entre duas esquinas em Roma, com base em uma tabela que descreve as conexões entre as ruas e estradas. A base de dados foi obtida do site da universidade de Roma, e está disponível ao público no link http://www.diag.uniroma1.it/challenge9/download.shtml. A base de dados contem informação de uma grande parcela das ruas/estradas de roma. Seus 3353 vértices representam esquinas e suas 8870 arestas representam ruas, estradas ou recortes destas. O grafo é conexo e possui pesos representando o comprimento das arestas em metros de maneira aproximada.  

Requisitos:
Python 3 e
Pandas

Como Usar:
Clone este repositório.
Execute rome_roads_bellman-ford.py e insira o índice do vértice de origem e destino. Se preferir uma saída de caminho mais curto no formato de uma lista de arestas, insira 'lista' como terceira entrada. Se preferir um texto mais amigável a leitura, insira 'texto'.
O código calculará o melhor caminho e exibirá a distância total.

Exemplos de Funcionamento:
Entrada: ![image](https://github.com/lucasmorais286/Projeto-de-Extra-o-de-Dados-com-Bellman-Ford/assets/102563264/2411233d-48e1-411c-9d3c-52911185a0b2)
Saída: ![image](https://github.com/lucasmorais286/Projeto-de-Extra-o-de-Dados-com-Bellman-Ford/assets/102563264/d05115de-c8fe-4546-b951-110ec50562a7)

Entrada:![image](https://github.com/lucasmorais286/Projeto-de-Extra-o-de-Dados-com-Bellman-Ford/assets/102563264/8819446b-f00c-4d0a-ad3c-47aef8eb7848)
Saída:![image](https://github.com/lucasmorais286/Projeto-de-Extra-o-de-Dados-com-Bellman-Ford/assets/102563264/5b51a752-3236-4d5b-820c-735dff2f932f)

Entrada:![image](https://github.com/lucasmorais286/Projeto-de-Extra-o-de-Dados-com-Bellman-Ford/assets/102563264/6990f69c-d0a2-46cf-8c68-0d6d20113e89)
Saída: ![image](https://github.com/lucasmorais286/Projeto-de-Extra-o-de-Dados-com-Bellman-Ford/assets/102563264/7713b1c6-4cd1-49e0-91c9-a065f3b07d61)
