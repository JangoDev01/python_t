import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
# print(df)


#########################################
"""
    Criando o objecto vetorizador 
        - convertendo para letras minusculas
        - removendo stop words especificadas em uma lista 
        - e mantendo apenas os termos que aparecem em pelo menos 2 documentos (min_df=2)
"""

vetorizador = CountVectorizer(
    lowercase=True,
    stop_words=['is', 'a', 'the', 'and', 'of', 'to', 'in', 'since', 'are', 'or', 'so', 'many'],
    min_df=2,
    dtype=np.int16
)

# obtendo o vocabulário

vetorizador.fit(df['texto'])
"""
    get_feature_names_out() ->
        retorna os termos do vocabulário que atendem aos critérios especificados sklearn
"""
print(vetorizador.get_feature_names_out()) #

# gerando a representação estruturada a partir do vocabulario ajustado
representacao = vetorizador.transform(df['texto'])
# a representação retornada é uma matriz em um formato esparso (posso gerar o array usando toarray())
# esparso -> matriz com muitos zeros, economiza memória...
print(representacao)

# a partir daqui podemos aplicar as funções de similaridades entre termos ou documentos
rep_array = representacao.toarray()
print(rep_array)


##########################################
"""
    -> from sklearn.metrics.pairwise import cosine_similarity <-
    função de coseno
        - mede a similaridade entre dois vetores no espaço n-dimensional
        - varia entre 0 e 1

"""
matrix_sim = cosine_similarity(rep_array)
print(matrix_sim)

# identificando o texto mais similar a um dado texto
def most_similar(id_doc, matrix):
    matrix_sim = cosine_similarity(matrix)
    best_sim = -1
    id_best_sim = -1

    for id, doc_sim in enumerate(matrix_sim[id_doc]):
        if id != id_doc:  # não comparar o documento com ele mesmo
            if doc_sim > best_sim:
                best_sim = doc_sim
                id_best_sim = id
    return id_best_sim

print(df)
print("-----------------------------")
doc_id = 1 # id do texto saido da nossa lista "texto" para comparar a similaridade

print(f"Texto: {df.loc[doc_id]['texto']}")
print(f"Texto mais similar: {df.loc[most_similar(doc_id, rep_array)]['texto']}")