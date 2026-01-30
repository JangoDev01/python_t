import numpy as np
import nltk

sintomas = ["Estou com dor de cabeça.",
            "Me diz oque fazer, chat.",
            "Tambem sinto tontura, muita tontura",
            "Estou com as pernas bambas,",
            "Minha boca esta seca.",
            "Parece urgente, parece muito urgente",
            "Devo ir ao medico ou me automedicar?",
            "Estou com medo,",
            "Por favor,",
            "Me diz oque fazer."
        ]

corpus_tok = []

def tokenize(texto):
    return nltk.word_tokenize(texto, language="portuguese")

for verso in sintomas:
    tokenizado = str(tokenize(verso.lower()))
    corpus_tok.append(tokenizado)

vocab = ['ao','com','dor','fazer','muito','seca','pernas','chat','parece','por','diz','me','medico','de','as','ir']

vetores = np.zeros((len(vocab), len(vocab)))

for verso in corpus_tok:
    for i, w1 in enumerate(vocab):
        for j, w2 in enumerate(vocab):
            if i != j:
                if w1 in verso and w2 in verso:
                    vetores[i, j] += 1

print(f"Vocabulario:\n {vocab} \n")
print(f"Matriz:\n {vetores} \n")
