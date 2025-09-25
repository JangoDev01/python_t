"""

x = float(input("digite o valor de x "))
y = float(input("digite o valor de y "))

z = round(x + y)
print(f"{z:,}")

"""

#  OU
#print(int(input("digite o valor de x ")) + int(input("digite o valor de y ")))

def main():
    x = int(input("digite o valor de x "))
    print("o valor de x ao quadrado e", quadrado(x))

def quadrado(x):
    return x * x

main()