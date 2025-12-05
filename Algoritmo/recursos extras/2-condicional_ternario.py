#### Operador condicional ternario

print('Comparando valores inteiros')

var1 = int(input('Digite um valor: '))
var2 = int(input('Digite um valor: '))

menor_valor = var1 if var1 < var2 else var2 # OCT
print(f'Primeiro valor: {var1}. \nSegundo valor: {var2} \nMenor valor: {menor_valor}')
print(f'Menor valor: {(var2, var1)[var1 < var2]}.')