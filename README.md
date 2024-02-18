Projeto Algoritmo de Bellman-Ford para Rotas em Roma
Este projeto utiliza o algoritmo de Bellman-Ford para encontrar o melhor caminho entre duas cidades em Roma, com base em uma tabela que descreve as conexões entre as estradas.

Requisitos:
Python 3
Pandas

Como Usar:
Clone este repositório.
Importe a tabela de estradas para o projeto.
Execute bellman_ford_roma.py e insira a cidade de origem e destino.
O código calculará o melhor caminho e exibirá a distância total.

Exemplo:
Considere a tabela de estradas:

Origem	Destino	Distância(peso)
A	         B	     10
A	         C	     15
B	         C	     5
B	         D	     20
C	         D	     10
O melhor caminho de A para D seria A -> B -> C -> D, com distância total de 35.
