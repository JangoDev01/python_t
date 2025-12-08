#### Exceções

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))

# try:
#     # codigo suspeito
#     r  = round(n1 / n2, 2)

# except ZeroDivisionError:
#     # tratamento da exceção 
#     print(f'Não é possivel dividir {n1} por {n2}!')

# else:
#     # opcional -- caso não houver erros 
#     print(f'O resultado de {n1} / {n2} Arredondado é: {r}')

def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            break
        except ValueError:
            print(f'Ocorreu um erro ao ler o valor.! Tente novamente.')

    try: 
        r = div(n1, n2)
    except ZeroDivisionError:
        print(f'Não é possivel dividir {n1} por {n2}!')
    except:
        print(f'Erro desconhecido')
    else:
        print(f'O resultado de {n1} / {n2} Arredondado é: {r}')
    finally:
        # rodará independentemente
        print(f'\n Fim do calculo!')
