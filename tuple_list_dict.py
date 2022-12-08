# TUPLES
# Crie uma tupla com pelo menos tres valores
# Imprima o segundo elemento da tupla
tup = ("a", "b", "c")
print(tup[1])

# Concatene a duas tuplas e a imprima
tup2 = 2,
tup3 = tup + tup2
print(tup3)

# Desconstrua os elementos da tupla e as imprima
primeiro, segundo, terceiro = tup
print(primeiro)
print(segundo)
print(terceiro)
print("----------------------------------------------------------------------")

# Verifique se uma determinada letra está numa string de uma tupla e imprima
nome = tuple("David")
print("a" in nome)

# Crie um tupla contendo todas as letras do nome execeto a primeira e imprima
print(nome[1:])
print("----------------------------------------------------------------------")


# LISTS
# Converta uma tupla em lista e imprima
tup = (1,2,3)
tup = list(tup)
tup[0] = 100
print(tup)
print("----------------------------------------------------------------------")

# Crie uma lista com dois elementos
# Adicione um elemento ao fim da lista usando .append()
# Adicione elementos usando .extend()
almoco = ["arroz", "feijao"]
almoco.append("batata")
almoco.extend(["pao", "pizza"])

# Imprima os dois primeiros elementos usando slicing notation
# Imprima a ultimo item usando index notation
print(almoco[:2])
print(almoco[0:2])
print(almoco[-1])
print("----------------------------------------------------------------------")

# Cria uma lista com diferentes itens e 
# verifique se a lista tem tres itens usando len()
refeicao = "ovos, frutas, laranja suco".split(", ")
print(refeicao)
print(len(refeicao) == 3)

# Crie uma nova lista usando list comprehension que terá
# o tamanho de cada elemento da primeira lista e imprima
tamanho = [len(item) for item in refeicao]
print(tamanho)
print("----------------------------------------------------------------------")


# DICTS
# Crie uma dicionario vazio
veiculos = {}

# Adicione alguns pares de chave-valor no dicionario
veiculos["Gol"] = "Ricardo"
veiculos["Onyx"] = "Janete"
veiculos["Kwid"] = "Simao"

# Verifique se "Gol" e "Lamborghini" existem; se nao, adicione
if "Gol" not in veiculos:
    veiculos["Gol"] = "Ninguém"
if "Lamborghini" not in veiculos:
    veiculos["Lamborghini"] = "Ninguém"

# Verifique para cada nome da lista
# for carro in ["Gol", "Lamborghini"]:
#    if not carro in motorista:
#        motorista[carro] = "Ninguém"


# Mostre todo conteudo do dicionario
def imprime_motorista():
    for carro, motorista in veiculos.items():
        print(f"{carro} é dirigido por {motorista}.")


imprime_motorista()
print("----------------------------------------------------------------------")

# Remova "Discovery" do dicionario
del veiculos["Lamborghini"]
imprime_motorista()
print("----------------------------------------------------------------------")

# Crie um dicionario usando dict()
veiculos = dict(
    [
        ("Gol", "Ricardo"),
        ("Onyx", "Janete"),
        ("Kwid", "Simao"),
    ]
)
imprime_motorista()
print("----------------------------------------------------------------------")
