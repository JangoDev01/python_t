from sklearn.preprocessing import OneHotEncoder
import nltk
from sklearn.feature_extraction.text import CountVectorizer

"""

"""
encod = OneHotEncoder(handle_unknown='ignore')

x = [['estou'],['com'],['dores'],['de'],['cabeça'],['desde'],['ontem'],['.']]

encod.fit(x)

vocab = list(encod.categories_[0])
vetores = encod.transform(x).toarray()

print(f"Vocabulario:\n {vocab} \n")
print(f"Matriz:\n {vetores} \n")

print(f"Atributos:\n {encod.get_feature_names_out()}") # mesma ordem do vocabulario

#############################################################

sintomas = ["Estou com dor de cabeça e minha cabeça não para de zumbir.",
            "Me diz oque fazer, chat.",
            "Tambem sinto tontura, muita tontura",
            "Estou com as pernas bambas, quase que não sinto minhas pernas",
            "Minha boca esta seca.",
            "Parece urgente, parece muito urgente",
            "Devo ir ao medico ou me automedicar?",
            "Estou com medo,",
            "Por favor,",
            "Me diz oque fazer."
        ]
print(len(sintomas))

def tokenize(texto):
    return nltk.word_tokenize(texto, language="portuguese")

vectorizer = CountVectorizer(tokenizer=tokenize, lowercase=True)

vector = vectorizer.fit_transform(sintomas)
vcb = vectorizer.get_feature_names_out()

print(f"Vocabularios:\n {vcb} \n")
print(f"Matriz:\n {vector.toarray()} \n")

