import math as m
import modulos_personalizados.mod_func as mf

## usando a função sqrt do módulo math para calcular a raiz quadrada de 16
print(m.sqrt(16))

## garante que o código só será executado se o script for executado diretamente
if __name__ == "__main__": 
    # eximbindo mensagem de boas vindas usando o módulo personalizado
    mf.boas_vindas()

    # calculando o fatorial de um numero usando o módulo personalizado
    print(f"\nCálculo de Fatorial")
    num = int(input("Digite um número inteiro para calcular o fatorial: "))
    fat = mf.fatorial(num)
    print(f"O fatorial de {num} é: {fat}")

    # exibindo a série de Fibonacci até um valor x usando o módulo personalizado
    print(f"\nSérie de Fibonacci")
    num2 = int(input("Digite um número inteiro para gerar a série de Fibonacci até esse valor: "))
    fib = mf.fibonacci(num2)
    print(f"A série de Fibonacci até {num2} é: {fib}")


