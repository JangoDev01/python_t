poema = """
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

########################################### tokenizando o corpus
import nltk
from nltk import tokenize
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE

# nltk.download('punkt')
# nltk.download('punkt_tab')

########################################### dividindo e armazenando o poema em diferentes sentenças

poema = poema.lower().split("\n")
# print(poema)

########################################### gerando os tokens

texto_tok = []
for verso in poema:
    tokens = tokenize.word_tokenize(verso, language="portuguese")
    texto_tok.append(tokens)

# print(texto_tok)

ngrams = 3
ngrams_pad, vocab = padded_everygram_pipeline(ngrams, texto_tok)

########################################### treinando o modelo de linguagem

lm = MLE(ngrams)
lm.fit(ngrams_pad, vocab) # fazendo os ajustes probabilisticos

"""
    gerando trechos de textos usando o metodo 
    lm.generate - recebe como parametro o tamanho da sequencia
            que a gente deseja gerar e o contexto, ou seja
            com base em algum token...
"""
texto_dig = str(input("Digite um palavra para ver o que vem a seguir: "))
print(lm.generate(5,text_seed=[texto_dig])) #
# print(lm.generate(5,text_seed=[texto_dig], random_seed=3)) # gera sempre os mesmos valores

##
texto_contexto = str(input(f"Digite um caractere de contexto para o calculo probabilistico: "))

### verificando a probabilidade de uma palvra
# print(lm.score(texto_dig))

### verificando a probabilidade de uma palvra depois de uma outra
print(f"As chances de {[texto_contexto]} aparecer depois de {[texto_dig]} é de: ", lm.score(texto_contexto, context=[texto_dig]))