## renomeando varios arquivos de uma so vez
import os

## mudando de diretorio
os.chdir('C:\\Users\\Administrator\\Dev Zone\\Python\\teste\\')
print(f'Diretorio atual: {os.getcwd()}')

padrao_nome = input('Qual o padrão de nomes de arquivos usar (sem a extensão)? ')

"""
    -loop para fazer uma interação por todos os itens desse diretorio...
    -quando o item for o arquivo ele será renomeado...
    -pra separar o nome da extensão
    -nessa interação teremos um contador pra enumerar os arquivos na renomeação
    -enumerate() -> recebe uma lista de itens e retorna um objeto enumeravel
        -muito usado em loops pra obter tanto os elementos que estão dentro de uma
        sequencia quanto os seus indeces açossiados...
    -os.listdir() -> lista o que esta dentro de um diretorio
        -contador -> será atribuido para cada elemento da lista um contador
        -arq -> um nome de arquivo tambem será atribuido...
"""
for contador, arq in enumerate(os.listdir()):
    # verifica se é realmente um arquivo
    if os.path.isfile(arq):
        # separa o nome do arquivo da extensão
        nome_arq, exten_arq = os.path.splitext(arq)
        # montando o nome que o usuario passou pro arquivo junto de sua enumeração, convertida pra string...
        nome_arq = padrao_nome + ' ' + str(contador)

        # montando o nome novo junto da extensão
        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)

print(f'\nArquivos renomeados!')