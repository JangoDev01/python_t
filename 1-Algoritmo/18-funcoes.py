#### funções

# sem parametros
def mensagem():
    print('Olá Mundo!')

## com parametros
def soma(a, b):
    print(a + b)

## retornando o valor de uma função pra dentro de uma variavel ou outra função
def mult(x, y):
    return x * y

##
def div(k, j):
    """
        Esse tratamento de erro previne o erro de divisão por 0
    """
    if j != 0:
        return k / j
    else:
        return 'Impossivel dividir por 0'

## 
def quad(val):
    quadrados = []
    for x in val:
        quadrados.append(x ** 2)

    return quadrados

if __name__ == '__main__':
    valores = [2,3,4,5,1,2,6,9,3,5]
    res = quad(valores)
    for g in res:
        print(g)