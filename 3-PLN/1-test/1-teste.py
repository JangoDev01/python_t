"""
    NLTK - Natural Language Toolkit
    Biblioteca para processamento de linguagem natural em Python.
    Tokenização
        - é um prcesso muito importante no PLN (Processamento de Linguagem Natural)
        - consiste em dividir um texto em unidades menores, chamadas tokens.
        - Esses tokens podem ser palavras, frases ou até mesmo caracteres individuais.
    Recursos adicionais
        - Conjuntos de dados (corpora)
            - Coleções de textos pré-existentes que podem ser usadas para treinamento e avaliação de modelos de PLN.
        - Ferramentas de pré-processamento
            - Funções para limpeza e preparação de texto, como remoção de stopwords, stemming e lematização.
    Documentação oficial
        - Site: https://www.nltk.org/

"""

import nltk # Biblioteca para processamento de linguagem natural
# nltk.download('machado') # Baixa o conjunto de dados 'machado' do NLTK
# nltk.download('punkt') # Baixa o conjunto de dados 'punkt' para tokenização
# nltk.download('punkt_tab') # Baixa o conjunto de dados 'punkt_tab' para tokenização com tabulação
# nltk.download('stopwords') # Baixa o conjunto de dados 'stopwords' do NLTK
from nltk.corpus import machado # Importa o corpus 'machado'
from nltk.corpus import stopwords # Importa o conjunto de dados 'stopwords'

"""
    Para retornar as stopwords de uma lingua específica, utilize:
        -stopwords.words('portuguese')
        -.words -> informa a string do idioma desejado
"""
print(stopwords.words('portuguese')) # Imprime as stopwords em português

# machado.fileids()[:3] # retorna os id dos arquivos do corpus 'machado'

# print(machado.raw('contos/macn001.txt')[:500]) # Imprime os primeiros 500 caracteres do arquivo 'contos-001.txt' do corpus 'machado'