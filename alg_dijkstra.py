#!/usr/bin/python3
# -*- coding: utf-8 -*-

DEFAULT_OUT = "out_alg_dijkstra.txt"
DEFAULT_SEED = None

# N seria o numero de vertices
DEFAULT_N_START = 10
DEFAULT_N_STOP = 20
DEFAULT_N_STEP = 1
DEFAULT_TRIALS = 3

from subprocess import Popen, PIPE
from time import sleep, time
from multiprocessing import Process
import shlex
import json

import sys
import os
import argparse
import logging
import subprocess

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import matplotlib.colors as colors
import matplotlib.cm as cmx

import gerador_grafos

import timeit

import networkx as nx


def dijkstra(graph, start, goal):
    shortest_distance = {}
    track_prodecessor = {}
    unseenNodes = graph
    infinity = 999999
    track_path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:

        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_prodecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_prodecessor[currentNode]
        except KeyError:
            print("path is not reachable")
            return []
            break

    track_path.insert(0, start)

    if shortest_distance[goal] != infinity:
        print("Shortest distance is " + str(shortest_distance[goal]))
        print("Optimal path is " + str(track_path))
        return track_path


def main():
    # Definição de argumentos
    parser = argparse.ArgumentParser(description='Dijkstra')
    help_msg = "arquivo de saída.  Padrão:{}".format(DEFAULT_OUT)
    parser.add_argument("--out", "-o", help=help_msg, default=DEFAULT_OUT, type=str)

    help_msg = "semente aleatória. Padrão:{}".format(DEFAULT_SEED)
    parser.add_argument("--seed", "-s", help=help_msg, default=DEFAULT_SEED, type=int)

    help_msg = "n máximo.          Padrão:{}".format(DEFAULT_N_STOP)
    parser.add_argument("--nstop", "-n", help=help_msg, default=DEFAULT_N_STOP, type=int)

    help_msg = "n mínimo.          Padrão:{}".format(DEFAULT_N_START)
    parser.add_argument("--nstart", "-a", help=help_msg, default=DEFAULT_N_START, type=int)

    help_msg = "n passo.           Padrão:{}".format(DEFAULT_N_STEP)
    parser.add_argument("--nstep", "-e", help=help_msg, default=DEFAULT_N_STEP, type=int)

    help_msg = "tentativas.        Padrão:{}".format(DEFAULT_N_STEP)
    parser.add_argument("--trials", "-t", help=help_msg, default=DEFAULT_TRIALS, type=int)

    # Lê argumentos from da linha de comando
    args = parser.parse_args()

    trials = args.trials
    f = open(args.out, "w")
    f.write("#Dijkstra Algorithm\n")
    f.write("#n time_s_avg time_s_std qnt_vertices qnt_arestas_avg (for {} trials)\n".format(trials))
    m = 100
    np.random.seed(args.seed)
    for n in range(args.nstart, args.nstop + 1, args.nstep):  # range(1, 100):  nstep é a qnt q incrementa por vez
        resultados = [0 for i in range(trials)]
        tempos = [0 for i in range(trials)]
        qnt_arestas = [0 for i in range(trials)]
        qnt_vertices = 0

        for trial in range(trials):
            print("\n-------")
            print("n: {} trial: {}".format(n, trial + 1))

            ###
            # criar o grafo de entrada do algoritmo aqui
            # ###
            num_vertices = n
            distancia_max = 100

            gerador = gerador_grafos.GeradorGrafo(args.seed)
            grafo = gerador.gerar_grafo(num_vertices, distancia_max)

            # gera a posição inicial aleatoria para o dijkstra
            x = np.random.randint(0, num_vertices - 1)

            # gera a posição final aleatoria para o dijkstra
            y = np.random.randint(0, num_vertices - 1)

            while x == y:
                if x != y:
                    break
                y = np.random.randint(0, num_vertices - 1)

            vertice_inicial = str(x)
            vertice_final = str(y)

            print("Entrada: {}".format(grafo))
            tempo_inicio = timeit.default_timer()
            resultados[trial] = dijkstra(grafo, vertice_inicial, vertice_final)  # usar algoritmo de dijkstra aqui
            tempo_fim = timeit.default_timer()
            tempos[trial] = tempo_fim - tempo_inicio

            qnt_arestas[trial] = gerador.qnt_arestas
            qnt_vertices = gerador.qnt_vertices
            print("Saída: {}".format(resultados[trial]))
            print('Tempo: {} s'.format(tempos[trial]))
            print("")


        tempos_avg = np.average(tempos)  # calcula média
        arestas_avg = np.average(qnt_arestas)   # calcula a média de arestas utilizadas nas tentativas
        tempos_std = np.std(a=tempos, ddof=False)  # ddof=calcula desvio padrao de uma amostra?

        f.write("{} {} {} {} {}\n".format(n, tempos_avg,
                                    tempos_std, qnt_vertices, arestas_avg))
    f.close()


if __name__ == '__main__':
    sys.exit(main())
