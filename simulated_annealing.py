# ALGORITMO: SIMULATED ANNEALING
import random
import math
import sys


# Neste caso e utilizado uma atualizacao da temperatura exponencial,
# para maior performance como mostrado em: https://pdfs.semanticscholar.org/e893/4a942f06ee91940ab57732953ec6a24b3f00.pdf
# k: decide o tamanho da "passada" da curva
# alpha: define a forma do decaimento da temperatura
# limit: numero de iteracoes
def exp_schedule(k=4, alpha=0.001, limit=20000):
    return lambda t: (k * math.exp(-alpha * t) if t < limit else 0)


def simulated_annealing(problem, schedule=exp_schedule()):
    current = problem.initial()
    current_h = problem.heuristic(current)
    for t in xrange(sys.maxsize):
        T = schedule(t)
        if T == 0 or problem.goal_test(current):
            return current
        neighbour = problem.randomNearState(current)
        if not neighbour:
            return current
        # OBS: problem.heuristic(state) retorna -h
        new_h = problem.heuristic(neighbour)
        delta_e = new_h - current_h
        # Tomada de decisao com base na variacao de energia e na probabilidade
        if delta_e > 0 or math.exp(delta_e / T) > random.uniform(0.0, 1.0):
            current = neighbour
            current_h = new_h
