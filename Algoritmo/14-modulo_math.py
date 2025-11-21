#### modulo math
import math

## # funções matemáticas internas do python
# valores = [4, -5, 0, 3.5, -2.8]
# print(max(valores))      # maior valor de uma lista
# print(min(valores))      # menor valor de uma lista

# a = -3
# b = 5
# c = 3.234567
# print(abs(a))            # valor absoluto
# print(pow(a, b))        # potência
# print(round(c))         # arredonda para o inteiro mais próximo

## # funções matemáticas via módulo (math)
x = 8
y = 15
z = 100

raiz_quadrada = math.sqrt(x)      # raiz quadrada
print(f"A raiz quadrada de {x} é: {raiz_quadrada}" )
print("função ceil: ",math.ceil(raiz_quadrada))   # arredonda para cima
print("função floor: ",math.floor(raiz_quadrada))  # arredonda para baixo
print("função round: ",round(raiz_quadrada, 2))    # arredonda para 2 casas decimais

logaritmo = math.log10(z)          # logaritmo natural (base 10)
print(f"O logaritmo de {z} é: {logaritmo}" )
print(math.pi)                     # valor de pi
print(math.factorial(x))       # fatorial de um número
print (x / math.inf)              # divisão por infinito 