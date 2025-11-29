#### Escopo

var_global = "Olá Mundo"

def msg():
    """
    se quisermos modificar o valor de uma variavel global dentro de uma rotina
    devemos deixar claro no codigo, se não fizermos isso o codigo vai apenas criar
    uma nova variavel local com o nome da variavel global...
    """
    global var_global
    var_global = "Olá Universo"
    var_local = "Programando em python"
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')

if __name__ == '__main__':
    print(f'Executando a função msg()')
    msg()
    print('Acessando as variável diretamente')
    print(f'Variável Global: {var_global}')