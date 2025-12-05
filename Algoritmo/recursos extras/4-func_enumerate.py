####

bebidas = ['Café', 'Chá', 'Água', 'Sumo', 'Refrigerante']

for indece, item in enumerate(bebidas):
    print(f'Índeces: {indece+1}, Item: {item}')

###
temperaturas = [12, 33, 3, 7, -3, 6, 11, -7, -5]
cidades = [
    'Luanda', 'Namibe', 'Kwanza-Sul', 'Huila',
    'Benguela', 'Huambo', 'Bie', 'Cunene', 'Bengo'
    ]
t_negativas = 0
t_positivas = 0

print(temperaturas)
for i, t in enumerate(temperaturas):
    if t < 0:
        t_negativas += 1
        print(f'A temperatura em {i} é negativa, com {t}Graus')
    if t > 0:
        t_positivas += 1
        print(f'A temperatura em {i} é positiva, com {t}Graus')

print(f'Há {t_negativas} temperaturas negativas na amostra')
print(f'Há {t_positivas} temperaturas positivas na amostra')