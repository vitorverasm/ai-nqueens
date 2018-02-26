# ALGORITMO: HILL CLIMBING GENERICO E HC COM RECOMECO ALEATORIO
from random import shuffle


def hill_climbing(problem):
    # Chama os neighboards com heuristica maior(pois usamos -h)
    current = problem.initial()
    while True:
        neighbours = problem.nearStates(current)
        if not neighbours:
            break
        # shuffle(neighbours)
        neighbour = max(neighbours, key=lambda state: problem.heuristic(state))
        if problem.heuristic(neighbour) <= problem.heuristic(current):
            break
        current = neighbour
    return current


# HC com random restart
def random_restart(problem, limit=10):
    state = problem.initial()
    count = 0
    while problem.goal_test(state) == False and count < limit:
        state = hill_climbing(problem)
        count += 1
    return state
