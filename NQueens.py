# MODELAGEM DO PROBLEMA DE N-RAINHAS
from random import choice
from collections import Counter
from random import randrange


# Classe generica de problemas de busca
class SearchProblem:
    # Inicia a busca(recebe os parametros iniciais)
    def __init__(self, initial=None):
        pass

    # Define o estado inicial
    def initial(self):
        pass

    # Teste de objetivo
    def goal_test(self, state):
        pass

    # Heuristica, utilizada para problemas de maximizacao ou minimizacao
    def heuristic(self, state):
        pass

    # Retorna os estados acessiveis a partir do estado atual
    def nearStates(self, state):
        pass

    # Retorna uma escolha aleatoria dentre os estados proximos
    def randomNearState(self, state):
        return choice(self.nearStates(state))


# Implementacao do modelo do problema das n-rainhas, sobrescrevendo a classe SearchProblem
class NQueensSearch(SearchProblem):
    # Modelo de um estado
    #
    # State: ([line_queens],
    #        (a, b, c),
    #        (h)
    #
    # Onde:
    # a: guarda o valor da coluna das rainhas
    # b: guarda l-c das rainhas
    # c: guarda l+c das rainhas
    # h: valor da heuristica do estado
    # A verificacao se da para cada rainha do tabuleiro, onde e testado
    # se existe outra rainha ja visitada com os mesmos valores de a,b,c.
    # caso exista, nao e um estado objetivo

    def __init__(self, N):
        self.N = N

    # Estado inicial:
    #   Retorna o estado inicial a partir do size
    def initial(self):
        return list(randrange(self.N) for i in range(self.N))

    # Teste de objetivo:
    #   Testa se alguma linha/coluna/diagonal e povoada por mais de uma rainha
    def goal_test(self, state):
        a, b, c = (set() for i in range(3))
        for row, col in enumerate(state):
            if col in a or row - col in b or row + col in c:
                return False
            a.add(col)
            b.add(row - col)
            c.add(row + col)
        return True

    # Heuristica: h
    #   Numero de pares de rainhas se atacando
    def heuristic(self, state):
        # define a,b,c como contadores
        a, b, c = [Counter() for i in range(3)]
        # contar quantas rainhas tem o os valores (a,b,c)
        # de forma que se obtem por exemplo quantas rainhas tem o valor de a=1
        for row, col in enumerate(state):
            a[col] += 1
            b[row - col] += 1
            c[row + col] += 1
        h = 0  # inicia as colisoes com 0
        # varre as estruturas de contagem (a,b,c) apenas incrementando o valor das colisoes
        # caso para algum valor de (a/b/c)>1 ja que e feito cnt[key]-1
        # divide para retirar contagens dobradas
        for count in [a, b, c]:
            for key in count:
                h += count[key] * (count[key] - 1) / 2
        return -h

    # Children ou estados vizinhos: children[]
    #   Retorna todos os estados acessiveis a partir do atual movendo as pecas por coluna
    def nearStates(self, state):
        near_states = []
        # Para cada state[coluna] verfica se as colunas vizinhas estao vazias
        for row in range(self.N):
            for col in range(self.N):
                # Se for diferente:
                #   entao a col atual da iteracao esta disponivel para movimentar-se
                #   visto que o state[] guarda o valor das colunas em que estao as rainhas
                if col != state[row]:
                    aux = list(state)
                    aux[row] = col  # Troca a coluna para a vazia
                    near_states.append(list(aux))  # E inclui na lista de nearStates
        return near_states
