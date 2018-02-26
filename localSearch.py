# CLASSE QUE REALIZA A BUSCA LOCAL
from time import time


class localSearch(object):
    def localSearch(self, problem, search_type, i):
        n_iterations = i
        cnt = 0
        start = time()
        s = []
        for i in range(n_iterations):
            result = search_type(problem)
            if problem.heuristic(result) is 0:
                cnt += 1
                s.append(result)
        print " - Hit rate: %2d/%d\tRuntime: %f" % (cnt, n_iterations, time() - start)
        return s
