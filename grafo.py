class Grafo:
    # Inicializa o grafo como um dicionário de arestas e guarda o número de vértices.
    def __init__(self, num_vertices):    
        self.num_vertices = num_vertices
        self.arestas = {}

    # Adiciona uma aresta. No dicionário, a aresta é representada por uma chave, que será uma dupla no formato(vértice_de_origem, vértice_destino), e uma chave que representa seu peso. O motivo para escolher esse modelo, é porque vai facilitar a construir uma lista de arestas a partir do caminho construído por predecessores mais adiante.
    def add_aresta(self, origem, destino, peso):
        self.arestas[(origem,destino)] = peso

    # Método que realizará o algoritmo de bellman-ford e construirá o caminho mais curto, assim como imprimirá os resultados.
    def bellman_ford(self, origem, destino,preferencia):
        # Inicializa as distâncias para todas as arestas como infinito e a origem como 0. O motivo do tamanho da lista ser num_vertices+1 é porque a identificação das arestas pare do 1 até o num_vertices, e não de 0 a num_vertices-1. Assim, para facilitar a chamada na lista, crio um espaço inútil na lista, distancais[0].
        distancias = [float('inf')] * (self.num_vertices+1)
        distancias[origem] = 0
        # Cria uma lista onde estarão representados os predecessores de cada vértice, considerando sempre o caminho mais curto da origem para eles. Naturalmente, o predecessor da origem será sempre None
        predecessores = [None]*(self.num_vertices+1)

        # Relaxa todas as arestas num_vertices - 1 vezes. 
        for i in range(self.num_vertices-1):
            # vertices recebe uma dupla que é posteriormente quebrada no v_origem e v_destino da aresta.
            for vertices, peso in self.arestas.items():
                v_origem = vertices[0]
                v_destino = vertices[1]
                # Se existe caminho para v_origem e o comprimento deste caminho somado ao peso desta aresta é menor do que o caminho atual do v_destino, um novo caminho mais curto é encontrado. Assim, a distância é atualizada.
                if distancias[v_origem] != float('inf') and distancias[v_origem] + peso < distancias[v_destino]:
                    distancias[v_destino] = distancias[v_origem] + peso
                    # Quando um caminho mais curto é encontrado, ao iterar sobre as arestas, o vértice destino tem seu predecessor atualizado para ser o vértice origem, que será seu predecessor no novo caminho mais curto.
                    predecessores[v_destino] = v_origem


        # Verifica se há ciclos negativos. Para a base de dados de estradas da cidade de Roma, que tem pesos exclusivamente positivos, será desnecessário, mas faz parte do algoritmo de Bellman-Ford. A ideia é testar se após relaxar o número máximo de vezes necessário, relaxar mais uma vez geraria uma redução de distâncias(o que só é possível se houverem ciclos de peso total negativo)
        for vertices, peso in self.arestas.items():
            v_origem = vertices[0]
            v_destino = vertices[1]
            if distancias[v_origem] != float('inf') and distancias[v_origem] + peso < distancias[v_destino]:
                print("Ciclo negativo!")
                return 0
        # Cria uma lista que vai agrupar o caminho mais curto para o vértice destino.
        caminho = []    
        # Partindo do vértice destino, começa um laço que só para quando chegar na origem(que tem como predecessor None). Para cada instância do laço, cria uma aresta como uma lista de 3 elementos [v_origem, v_destino, peso_da_aresta].
        vertice_atual = destino 
        while predecessores[vertice_atual] is not None:
            aresta = [predecessores[vertice_atual],vertice_atual,self.arestas[(predecessores[vertice_atual],vertice_atual)]]
            caminho.append(aresta)
            vertice_atual = predecessores[vertice_atual]
        # Ao fim do laço, caminho agora é uma lista das arestas na ordem invertida, então precisa ser revertido.    
        caminho.reverse()

        # Imprime os resultados de acordo com a preferencia.
        if preferencia == 'lista':
            print(f'Distância aproximada percorrida no menor caminho(metros): {distancias[destino]}')
            print(f'Caminho mais curto, representando pela sequência de ruas(arestas) a serem percorridas e seus respectivos comprimentos aproximados: {caminho}')
        if preferencia == 'texto':
            print(f'Você está em {origem}')
            for v_origem, v_destino, peso in caminho:
                print(f'Vá de {v_origem} para {v_destino}. peso: {peso} metros')
            print(f'Você chegou em {destino}. Você percorreu uma distância total de: {distancias[destino]} metros')
