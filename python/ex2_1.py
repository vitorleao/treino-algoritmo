from decimal import Decimal, getcontext

qtd = 4
soma = Decimal(0)
final = Decimal(7)
getcontext().prec = 2

for i in range(qtd):
    while True:
        nota = Decimal(input("Digite sua nota: "))
        if nota >= 0 and nota <= 10:
            soma += nota
            break
media = soma / qtd

if media >= final:
    print("Voce está aprovado. Sua media foi de:", media)
else:
    print("Voce está reprovado. Sua media foi de:", media)
