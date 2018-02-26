# N-Queen problem solver
## Description/Descrição:
This is a n-queen problem solver using local search algorithms.

[Pt-Br]:
Este é um programa que resolve o problema das n-rainhas utilizando algoritmos de busca local.

### Local search algorithms/Algoritmos de busca local:

- Hill Climbing
- Hill Climbing with random restart
- Simulated Annealing

### Heuristic/Heurística:

To solve this problem we used as a heuristic the number of pairs of queens attacking each other, either directly or indirectly.

[Pt-Br]:
Para resolver este problema utilizou-se como heurística, o número de pares de rainhas se atacando, seja direta ou indiretamente.

### Usage/Modo de uso:

```bash
python main.py -h
usage: main.py [-h] [-n N] [-i I] [--all {0,1}]

N-queens problem solver by using local search algorithms. Author: Vitor Veras.
Default arguments: -n=8 ; -i=10 ; --all=0

optional arguments:
  -h, --help   show this help message and exit
  -n N         Size of the board
  -i I         Number of iterations
  --all {0,1}  0 = show one solution | 1 = show all solutions
```
### Default output/Saída padrão:

```bash
python main.py
python main.py
hill_climbing
 - Hit rate:  2/10	Runtime: 0.038855
. . . . . Q . .
. Q . . . . . .
. . . . . . Q .
Q . . . . . . .
. . Q . . . . .
. . . . Q . . .
. . . . . . . Q
. . . Q . . . .


hc_random_restart
 - Hit rate:  9/10	Runtime: 0.196223
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .
Q . . . . . . .
. . . . . . . Q
. . . . Q . . .
. . Q . . . . .
. . . . . Q . .


simulated_annealing
 - Hit rate: 10/10	Runtime: 0.779093
. . . Q . . . .
. . . . . . Q .
. . Q . . . . .
. . . . . . . Q
. Q . . . . . .
. . . . Q . . .
Q . . . . . . .
. . . . . Q . .


```
### obs: All code comments are in Brazilian Portuguese.

## Author

* **Vitor Veras de Moura** - [GitHub](https://github.com/vitor-veras) - Email: vitorverasm@gmail.com
