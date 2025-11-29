#### Funções Especiais: lambda, map, filter, reduce ####

## # funções lambda ##########################################

# # o quadrado de um numero
# quadrado = lambda x: x**2
# for i in range(1, 4):
#     print(quadrado(i))

# # verifica se um numero é par
# par = lambda x: x %2 == 0
# print(par(8))

# # converte de fahrenheit pra celcios
# f_c = lambda f: (f - 32) * 5/9
# print(f_c(122))

## # função map ##########################################

# num = [1,2,3,4,5,6,7,8,9,10]
# """
# a função map aplica uma função a cada item de um iterável (lista, tupla, etc) e retorna um map object (um iterador)
# """
# dobro = list(map(lambda x: x*2, num))
# print(dobro)

# #
# palavras = ['python', 'é', 'uma', 'linguagem', 'de', 'programação', 'muito', 'boa']
# maiusculas = list(map(str.upper, palavras))
# print(maiusculas)

## # função filter ##########################################

def numero_par(n):
    return n % 2 == 0
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
num_par = list(filter(lambda n: n % 2 == 0, numeros))
print(num_par)

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
num_impar = list(filter(lambda n: n % 2 != 0, numeros))
print(num_impar)

## # função reduce ##########################################
from functools import reduce

def mult(x, y):
    return x * y

numeros = [1,3,7,8,5,6]
total = reduce(mult, numeros)
print(total)

numeros = [1,2,3,4]
total = reduce(lambda x, y: x**2 + y**2, numeros)
print(total)
