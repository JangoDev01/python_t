#### modulos com funções variadas para serem importadas em outros scripts

## função para exibir mensagem de boas vindas
def boas_vindas():
    print("Seja Bem Vindo ao Treinamento de Python!")

## função para exibir mensagem de despedida
def despedida():
    print("Obrigado por participar do Treinamento de Python. Até a próxima!")

## função que calcula o fatorial de um número
def fatorial(numero):
    if numero < 0:
        return "Digite um numero maior ou igual a zero"
    elif numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

## função para retornar uma série de Fibonacci de até um valor x
def fibonacci(n):
    resultado = []
    a, b = 0, 1
    while b <= n:
        resultado.append(b)
        a, b = b, a+b
    return resultado