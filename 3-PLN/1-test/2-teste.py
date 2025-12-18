"""
Exemplo de tokenização de texto usando NLTK em Python.
    - word_tokenize: tokenização por palavras
    - sent_tokenize: tokenização por sentenças
    - TweetTokenizer: tokenização para textos de redes sociais
        - mais adequado para textos curtos e informais, como tweets.
        - lida melhor com abreviações, hashtags, menções e emoticons.
"""

from nltk.tokenize import word_tokenize # Importa a função de tokenização por palavras
from nltk.tokenize import sent_tokenize # Importa a função de tokenização por sentenças
from nltk.tokenize import TweetTokenizer # Importa o tokenizador para tweets

# criando texto de exemplo
texto = "Olá, mundo! Este é um exemplo de tokenização. Vamos dividir este texto em tokens."
texto_tweet = "Adoooooooooooooro programar em Python vivaaaaaaaa! #coding @python_dev :)"

# Tokenização por palavras
tkn_palavras = word_tokenize(texto, language='portuguese') # Tokeniza o texto em palavras
print(f"Tokenização por palavras: {tkn_palavras}")

# Tokenização por sentenças
tkn_sentencas = sent_tokenize(texto, language='portuguese') # Tokeniza o texto em sentenças
print(f"Tokenização por sentenças: {tkn_sentencas}")

# Tokenização para tweets
"""
    - strip_handles=True: remove menções (handles) do Twitter
    - reduce_len=True: reduz a repetição de caracteres (ex: "coooool
"""
tkn_tweet = TweetTokenizer(strip_handles=True, reduce_len=True) # Cria uma instância do TweetTokenizer
print(f"Tokenização para tweets: {tkn_tweet.tokenize(texto_tweet)}") # Tokeniza o texto do tweet
