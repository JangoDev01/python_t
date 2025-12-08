#### Parametros

## 
"""
parametros com valores padrão:
    valores atribuidos dentro da lista de argumentos ao definir a função
caso não for atribuido nenhum valor, esses valores pre definidos serão exibidos... 
"""
def contar(num=11, caractere='o_o'):
    for i in range(1, num):
        print(f'{i} - {caractere}')

##
x = 3
y = 6
z = 9

def soma_mult(a, b, c = 0):
    if c == 0:
        return a * b
    else:
        return a + b + c


if __name__ == '__main__':
    #
    contar()
    contar(4, '&&@@')

    res = soma_mult(x, y, z)
    print(res)
