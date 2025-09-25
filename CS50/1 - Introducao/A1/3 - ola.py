def main():
    helo()
    print("===========================")
    name = input("Qual e o seu nome? ")
    helo(name)

def helo(to="Mundo"):
    print(f"Ola, {to}")

main()