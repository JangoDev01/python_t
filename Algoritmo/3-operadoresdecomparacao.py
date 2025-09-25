# Operadores de comparação

u = v = w = x = y = z = False
n1 = n2 = 0

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

print("\n")

u = n1 == n2 
print("São iguais?", u, "\n") 

v = n1 > n2
print(n1, "é maior que", n2, "?", v, "\n")

w = n1 < n2
print(n1, "é menor que", n2, "?", w, "\n")

x = n1 >= n2
print(n1, "é maior ou igual a", n2, "?", x, "\n")

y = n1 <= n2
print(n1, "é menor ou igual a", n2, "?", y, "\n")

z = n1 != n2
print("São diferentes?", z)   

