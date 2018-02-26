from random import choice


# METODO PARA IMPRESSAO DO TABULEIRO
def printBoard(result, param):
    # Se a lista de resultados for vazia(ex: hc pode retornar lista vazia)
    if not result:
        print([None])
    # Se tiver resultados e --all = 0
    if param == 0 and result:
        r = choice(result)
        # print r
        board = []
        for col in r:
            line = ['.'] * len(r)
            line[col] = 'Q'
            board.append(str().join(line))

        charlist = map(list, board)
        for line in charlist:
            print " ".join(line)
    # Se tiver resultados e --all = 1
    else:
        # print result
        board = []
        for r in result:
            for c in r:
                line = ['.'] * len(r)
                line[c] = 'Q'
                board.append(str().join(line))

        charlist = map(list, board)
        for i in range(0, len(charlist)):
            if i % len(charlist[i]) == 0:
                print "\n"

            print(" ".join(charlist[i]))
    print "\n"
