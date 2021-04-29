# fonte: https://stackoverflow.com/questions/18651871/generating-a-map-graph-for-a-traveling-salesmanproblem-python
import math
import numpy as np


class GeradorGrafo():
    def __init__(self, seed):
        self.seed = seed
        self.qnt_vertices = 0
        self.qnt_arestas = 0

    def gerar_grafo(self, num_vertices, distancia_max):
        grafo = self.planar_graph_generator(num_vertices, distancia_max)
        grafo = self.traduzir_grafo(grafo)
        return grafo

    def traduzir_grafo(self, grafo):
        self.qnt_vertices = len(grafo)
        novo_grafo = {}
        for i in range(self.qnt_vertices):
            arestas_de_i = {}
            for j in range(self.qnt_vertices):
                if grafo[i][j] > 0:
                    arestas_de_i.update({str(j): grafo[i][j]})
                    self.qnt_arestas += 1
            novo_grafo.update({str(i): arestas_de_i})
        return novo_grafo

    def planar_graph_generator(self, qnt_vertices, distancia_vertices):
        np.random.seed(self.seed)
        points = [[np.random.randint(0, distancia_vertices), np.random.randint(0, distancia_vertices)] for i in
                  range(qnt_vertices)]
        graph = [[self.dist(points[i], points[j]) for i in range(qnt_vertices)] for j in range(qnt_vertices)]
        print("points: ", points)
        print("graph: ", graph)
        return graph

    def dist(self, a, b):
        return round(math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2))
