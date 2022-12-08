from decimal import Decimal, getcontext

qtd = 5
cont = 0
maior = Decimal(0)
getcontext().prec = 2

while True:
    valor = Decimal(input("Digite um valor: "))
    if valor >= 0 and valor > maior:
        maior = valor
        cont += 1
    if cont > qtd:
        break

print("O maior valor é:", maior)
