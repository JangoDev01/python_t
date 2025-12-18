import pandas as pd
import numpy as np

texto = [
    'Goku is a hero in the Dragon Ball since 1989.',
    'The seven Dragon Balls can make wishes come true.',
    'If the wishes are superfuous, the dragon balls will became dark.',
    'Seiya is a bronze knight and is one of the main knights of the zodiac.',
    'A knight of the zodiac wear a bronze, silver or gold cloth to protect Athena.',
    'Saint Seiya: Knights of the Zodiac is a popular anime and manga series.'
]

classes = ['Dragon Ball', 'Dragon Ball', 'Dragon Ball', 'Cav. Zod.', 'Cav. Zod.', 'Cav. Zod.']

df = pd.DataFrame({'texto': texto, 'classes': classes})
print(df)

### baseada em caracteres ## A distancia de Levenshtein -> mede a diferença entre duas sequências

def Levenshtein(seq1, seq2):
    # Cria uma matriz
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))

    # setar os valores das colunas (0, n-1)
    for x in range(size_x):
        matrix[x, 0] = x

    # setar os valores das linhas (0, m-1)
    for y in range(size_y):
        matrix[0, y] = y

    # calcular a distancia 
    for x in range(1, size_x):
        for y in range(1, size_y):
            # se os caracteres são iguais, não aumenta a distancia
            if seq1[x-1] == seq2[y-1]:
                matrix[x, y] = matrix[x-1, y-1]

            # se são diferentes, aumenta a distancia em 1
            else:
                matrix[x, y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1] + 1,
                    matrix[x, y-1] + 1
                )

    """
        list(seq1) -> converte a string em uma lista de caracteres
    """
    print(pd.DataFrame(matrix[1:,1:], index=list(seq1), columns=list(seq2)))

    return (matrix[size_x - 1, size_y - 1])

# Levenshtein('medicina', 'medico')
print('---------')
doc_id_a = 3 # id do texto 4 saido da nossa lista "texto"
doc_id_b = 1 # id do texto 2 saido da nossa lista "texto"
print(f'Texto 1: {df.loc[doc_id_a]["texto"]}')
print(f'Texto 2: {df.loc[doc_id_b]["texto"]}')
print('---------')

Levenshtein(df.loc[doc_id_a]["texto"], df.loc[doc_id_b]["texto"])

### baseada em termos ##