# PERGUNTAR O NOME DO USUARIO, REMOVE ESPACOS DA STRING E CONVERTE AS INICIAIS EM MAIUSCULAS
nome = input("Qual é o seu nome ").strip().title()

# DIVIDIR O NOME EM SUBSTRINGS COM BASE NO ESPACAMENTO / primeiro e o ultimo 
first, last = nome.split()

# IMPRIMIR NA TELA O NOME DO USUARIO COM SAUDACAO
print(f"Ola, {first}")
""" 
OU 
print(f"Ola, ", nome)

"""