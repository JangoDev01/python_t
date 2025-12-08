####

### Ler conteudo de arquivos de texto

# manipulador = open('C:\\Users\\Administrator\\Dev Zone\\Python\\arquivos teste pra manipulacao\\arquivo_teste.txt', 'r', encoding='utf-8')

## ler todo o conteudo de texto do arquivo 
# print(f'\nMétodo read():\n')
# print(manipulador.read())

## retornando linha por vez
# print(f'\nMétodo readline():\n')
# print(manipulador.readline())
# print(manipulador.readlines())

# texto_termo = input('Qual termo deseja buscar no arquivo? ')

# try:
#     manipulador_leitor = open('C:\\Users\\Administrator\\Dev Zone\\Python\\arquivos teste pra manipulacao\\arquivo_teste.txt', 'r', encoding='utf-8')
#     for linha in manipulador_leitor:
#         """
#             -retira o ultimo caractere da linha que nesse caso é a quebra
#             de linha...
#         """
#         linha = linha.rstrip()
#         if texto_termo in linha:
#             print(f'A string foi encontrada!')
#             print(f'{linha}\n')
#         else:
#             print(f'String não encontrada')
# except IOError:
#     print(f'Não foi possível abrir o arquivo')
# else:
#     """
#         -liberando o arquivo dos precessos do OS pra não dar erro de uso em curso
#         -liberando tambem memoria
#     """
#     manipulador_leitor.close()

# ### Escrever em arquivos de texto
# texto_escrito = input('Digite o texto que deseja adicionar no arquivo: ')

# try:
#     manipulador_escritor = open('C:\\Users\\Administrator\\Dev Zone\\Python\\arquivos teste pra manipulacao\\arquivo_teste.txt', 'a', encoding='utf-8')
#     manipulador_escritor.write(f'\n{texto_escrito}')
#     print(texto_escrito)
# except IOError:
#     print(f'Não foi possível abrir o arquivo')
# else:
#     manipulador_escritor.close()

### Criar e escrever no arquivo de texto
print(f'==========Criador de arquivos de texto (txt, word, html...)==========\n')
nome_arquivo = input('Digite o nome do arquivo (sem espaçamento no nome): ')
texto_escrito = input('Digite o texto que deseja adicionar no arquivo: ')

try:
    criador_de_arquivos = open(f'C:\\Users\\Administrator\\Dev Zone\\Python\\arquivos teste pra manipulacao\\{nome_arquivo}', 'w', encoding='utf-8')
    criador_de_arquivos.write(f'\n{texto_escrito}')
except IOError:
    print(f'Não foi possível criar o arquivo')
else:
    criador_de_arquivos.close()

# Ler o arquivo
try:
    criador_de_arquivos = open(f'C:\\Users\\Administrator\\Dev Zone\\Python\\arquivos teste pra manipulacao\\{nome_arquivo}', 'r', encoding='utf-8')
    print(f'\nExibindo o conteudo do arquivo {nome_arquivo}: \n{criador_de_arquivos.read()}')
except IOError:
    print(f'Não foi possível criar o arquivo')
else:
    criador_de_arquivos.close()
