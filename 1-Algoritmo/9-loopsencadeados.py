#### LOOPS Encadeados

## Loop encadeado para repetir ações dentro de outras ações.
# for cont_externo in range(1, 6):
#     print(f'\nRodada: {cont_externo}')

#     for cont_interno in range(5, 0, -1): ## Contagem regressiva
#         print(f'Valor: {cont_interno}')

# print('\nFim do Programa!')

##################################################

## Loop encadeado que sorteia valores aleatórios
import random

for A in range(1, 6):
    print(f'\nConjunto {A}')
    for B in range(5):
        numero_aleatorio = random.randint(1, 10)
        print(f'Valor: {numero_aleatorio}')
