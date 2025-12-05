#### Gerenciamento de contexto com a palavra chave with

## forma normal
try:
    open_file = open(f'C:\\Users\\Administrator\\Dev Zone\\Python\\arquivos teste pra manipulacao\\arquivo_teste.txt', 'r', encoding='utf-8')
    print(f'Forma normal: \n{open_file.read()}')
except:
    print(f'Não foi possível abrir o arquivo')
else:
    open_file.close()

## usando o GC with
cont = 0
with open(f'C:\\Users\\Administrator\\Dev Zone\\Python\\arquivos teste pra manipulacao\\arquivo_teste.txt', 'r', encoding='utf-8') as file:
    for linha in file:
        cont += 1
        print(f'Forma with{cont}: \n{linha}')