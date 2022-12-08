name = input("Qual o seu nome?")
print("Olá " + name) if len(name) > 0 else print("Olá desconhecido")


# if len(name) == 0:
#     name = 'desconhecido'
# print("Olá " + name)

if not name:
    name = 'desconhecido'
print("Olá " + name)

print("Olá " + (name or 'desconhecido'))

print(name.upper() if name else 'desconhecido')
# 0
# None
# ''
# []
# {}

# print("Olá " + name) if len(name) > 0 else print("Olá desconhecido")
# print("Olá " + name) if len(name) else print("Olá desconhecido")
print("Olá " + name if name else "Olá desconhecido")
