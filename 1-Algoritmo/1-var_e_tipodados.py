# ctrl + k + c == comenta o codigo
# ctrl + k + u == descomenta o codigo
nome_usuario = "Miguel"
idade_usuario = 20
media = 10.2
n1 = n2 = n3 = 2
estado = True 

dia_da_semana = "Segunda-feira"
dia = 10


print(nome_usuario)
print(idade_usuario)

# funcao type() == mostra o tipo de dado da variavel
# print(type(media))
# print(type(n1))
# print(type(n2))
# print(type(n3))
# print(type(nome_usuario))
# print(type(idade_usuario))
# print(type(estado))
# print(type(1+2j))  # numero complexo para calculos matematicos de circuitos eletricos
# print(type([1,2,3]))  # lista para dados mutaveis
# print(type((1,2,3)))  # tupla para dados imutaveis
# print(type({1,2,3}))  # conjunto para dados nao repetidos
# print(type({"nome":"Miguel", "idade":20}))  # dicionario para dados em pares chave-valor

# funcao isinstance() == verifica se a variavel é do tipo especificado
print(isinstance(dia_da_semana, str))
print(isinstance(media, (int, float)))

a = 30
b = 2
r = a * b
print(r)