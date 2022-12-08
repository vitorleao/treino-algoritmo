name = input("Qual o seu nome?")
if len(name) <= 0:
    name = "desconhecido"
print("Olá " + name.lower())