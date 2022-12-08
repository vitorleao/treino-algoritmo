from decimal import Decimal, getcontext

qtd = 4
soma = Decimal(0)
final = Decimal(7)
getcontext().prec = 3

for i in range(qtd):
    nota = input("Digite sua nota: ")
    soma += Decimal(nota)
media = soma / qtd

if media >= final:
    print("Voce está aprovado. Sua media foi de:", media)
else:
    print("Voce está reprovado. Sua media foi de:", media)
