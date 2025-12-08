#### Recursividade

"""
Fórmula geral para o fatorial
CASO BASE:
    fatorial(num) = 1, se num = 0 ou se num = 1
CASO RECURSIVO:
    fatorial(num) = num * fatorial(num -1), para num > 1       ==>
        um valor * o seu antecessor
        4! -> 4 * fatorial(4 - 1)
"""

def fact_rec(num):
    if num == 0 or num == 1:
        return 1

    else:
        return num * fact_rec(num - 1)

if __name__=='__main__':
    x = int(input(f'Digite um número inteiro positivo para calcular o seu fatorial: '))
    try:
        res = fact_rec(x)
    except RecursionError:
        print(f'O número fornecido é negativo ou muito grande!')
    else:
        print(f'O fatorial de {x} é {res}')
