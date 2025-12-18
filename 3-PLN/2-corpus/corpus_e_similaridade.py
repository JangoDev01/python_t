poema_corpus = """
    No silêncio da noite, onde as estrelas dançam,
    O vento sussurra segredos antigos ao mar.
    As ondas quebram em ritmos ancestrais,
    Carregando histórias de amores perdidos e reencontrados.

    Sob o céu de veludo, pontilhado de luzes distantes,
    A lua observa, guardiã dos sonhos adormecidos.
    Florestas murmuram canções de folhas caídas,
    E rios serpenteiam por vales de mistério profundo.

    O coração humano, um labirinto de emoções,
    Pulsa ao compasso do universo em expansão.
    Alegrias efêmeras, dores que marcam a alma,
    Tecem a tapeçaria da existência efêmera.

    Nas montanhas altivas, onde o ar é puro e frio,
    Águias planam livres, desafiando as alturas.
    Homens e mulheres buscam o cume da verdade,
    Mas tropeçam em pedras de dúvidas e ilusões.

    O tempo, inexorável, devora os instantes,
    Transformando memórias em poeira estelar.
    No entanto, o amor permanece, eterno farol,
    Guiando almas perdidas de volta ao lar.

    Nas ruas da cidade, onde o caos reina soberano,
    Pessoas correm atrás de sombras fugazes.
    Sonhos se entrelaçam com a realidade dura,
    Criando mundos paralelos de esperança e desespero.

    A primavera floresce em cores vibrantes,
    Anunciando renascimento e possibilidades infinitas.
    Borboletas dançam em jardins perfumados,
    Enquanto o sol beija a terra com raios dourados.

    No inverno gelado, quando o mundo se cala,
    Neve cobre feridas antigas com manto branco.
    Reflexões profundas emergem do silêncio,
    Revelando verdades ocultas no fundo da alma.

    Assim, o ciclo da vida continua incessante,
    Um poema escrito nas estrelas e na terra.
    Cada verso, uma lição; cada rima, uma conexão,
    Unindo o finito ao infinito, em harmonia eterna.

    Nas profundezas do oceano, onde criaturas estranhas habitam,
    Corais coloridos abrigam segredos submersos.
    Peixes nadam em balés aquáticos graciosos,
    Contando lendas de tesouros perdidos no abismo.

    O fogo da paixão queima intenso e voraz,
    Consumindo barreiras e acendendo chamas.
    Mas cuidado, pois o excesso pode destruir,
    Deixando cinzas onde outrora floresceu a vida.

    Nas planícies vastas, onde o horizonte se perde,
    Cavaleiros solitários buscam destinos incertos.
    Ventos carregam sussurros de profecias antigas,
    Guiando passos rumo a aventuras desconhecidas.

    A música do universo ressoa em cada nota,
    Harmonizando caos e ordem em sinfonia perfeita.
    Notas altas e baixas, ritmos acelerados e lentos,
    Criando melodias que tocam o coração humano.

    No final, quando as cortinas se fecham,
    E o palco da vida se esvazia lentamente,
    Lembramos que cada momento é um verso precioso,
    Num poema eterno, escrito pelo tempo e pelo amor.
"""

import pandas as pd
import numpy as np
import nltk
from nltk import tokenize

## 
tokens = tokenize.word_tokenize(poema_corpus, language='portuguese')
tokens_minusculas = tokenize.word_tokenize(poema_corpus.lower(), language='portuguese')

vocabulario = set(tokens_minusculas)

print(f'Tamanho do corpus (número de tokens): {len(tokens)}')
print(f'Tamanho do vocabulário (número de tokens únicos): {len(vocabulario)}')

# print(tokens)
# print(len(tokens))

# print(vocabulario)
# print(len(vocabulario))

# sentencas = nltk.sent_tokenize(poema_corpus, language='portuguese')
# print(sentencas)
# print(f'Tamanho do corpus (número de sentenças): {len(sentencas)}')

######################## similaridades ########################

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