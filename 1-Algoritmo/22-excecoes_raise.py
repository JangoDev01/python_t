#### Forçar uma exceção
from math import sqrt

class NumeroNegativoError(Exception):
    def __init__(self):
        pass # ignore e passe adiante

if __name__ == '__main__':
    print('\tCalculadora de raiz quadrada \n')
    try:
        num = int(input(f'Digite um número positivo: '))
        if num < 0:
            raise NumeroNegativoError
    except NumeroNegativoError:
        print(f'Foi fornecido um número negativo: {num}')
    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)}')
    finally:
        print(f'Fim do calculo')
