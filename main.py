# MAIN CLASS
import argparse
from printBoard import printBoard
from localSearch import localSearch
from hill_climbing import hill_climbing
from hill_climbing import random_restart
from simulated_annealing import simulated_annealing
from NQueens import NQueensSearch

if __name__ == "__main__":

    # Parametros
    str = "N-queens problem solver by using local search algorithms.\n\t Author: Vitor Veras.\t Default arguments: -n=8 ; -i=10 ; --all=0"
    parser = argparse.ArgumentParser(description=str)
    parser.add_argument("-n", type=int, default=8, help="Size of the board")
    parser.add_argument("-i", type=int, default=10, help="Number of iterations")
    parser.add_argument("--all", type=int, dest='all', action='store',
                        choices=range(0, 2), default=0,
                        help="0 = show one solution | 1 = show all solutions")
    args = parser.parse_args()

    # Inicia a busca
    test = localSearch()
    # Inicia o problema passando o tamanho do tabuleiro
    problem = NQueensSearch(args.n)
    algorithms = [hill_climbing, random_restart, simulated_annealing]
    names = ["hill_climbing", "hc_random_restart", "simulated_annealing"]
    problems = [problem, problem, problem]
    for i in range(len(algorithms)):
        print names[i]
        result_board = test.localSearch(problems[i], algorithms[i], args.i)

        # Imprime um tabuleiro com base no argumento --all passado
        printBoard(result_board, args.all)
