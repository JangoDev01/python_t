import os

## 
os_name = os.name
print(f'String que para dizer o sistema operacional: {os_name}')

## pegando o diretorio atual
diretorio_atual = os.getcwd()
print(f'Diretorio atual: {diretorio_atual}')

## atalho para o diretorio atual ==> representado por um "."
atalho_pro_diretorio_atual = os.curdir
print(f'Atalho pro diretorio atual: {atalho_pro_diretorio_atual}')

## visualizando o conteudo do diretorio atual
listando_tudo_no_diretorio_atual = os.listdir()
print(f'Lista de tudo no diretorio atual: {listando_tudo_no_diretorio_atual}')

## navegando pelos diretorios
navegando_pelos_diretorios = os.listdir('c:\\')
print(f'Navegando em outros diretorios: {navegando_pelos_diretorios}')

# mudando de diretorio ==> o caminho para o novo diretorio deve ser absoluto
mudando_de_diretorio = os.chdir('c:\\')
print(f'Mudando de diretorio: {mudando_de_diretorio}')

###
"""
    Todo comando daqui pra baixo foi executado no terminal e
    colocado aqui como forma de documentação ou anotações...
    Sigam Meus Bons!
"""

## criando uma pasta
# os.mkdir('teste')

## montando um caminho usando variaveis --> terminal
# pasta_nova = 'teste3'
# pasta_pai = 'C:\\Users\\Administrator\\Dev Zone\\Python\\teste\\' 
# caminho_completo = os.path.join(pasta_pai, pasta_nova)

## mudar o nome da pasta
# os.rename('c:\\teste2', 'c:\\teste10')

## apagar uma pasta
# os.rmdir('c:\\teste10')

## verificar nome de pasta ou arquivo sem o caminho completo
# os.path.basename(os.getcwd())

## verificar o nome do diretorio atual
# os.path.dirname(os.getcwd())

## criando diretorios de forma recursia
# pasta_pai = os.getcwd()
# novas_pastas = 'python\\poo\\IA'
# caminho = os.path.join(pasta_pai, novas_pastas)
# print(caminho)
# os.makedirs(caminho)

## verificando se o caminho existe
# os.path.exists('C:\\Users\\Administrator\\Dev Zone\\Python\\teste\\') 

## verificando se é um diretorio ou um arquivo
# os.path.isdir('C:\\Users\\Administrator\\Dev Zone\\Python\\teste\\')
# os.path.isfile('C:\\Users\\Administrator\\Dev Zone\\Python\\teste\\') 