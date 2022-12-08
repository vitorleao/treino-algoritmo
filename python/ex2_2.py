from decimal import Decimal, getcontext

qtd = 0
soma = Decimal(0)
final = Decimal(7)
getcontext().prec = 2

while True:
    nota = Decimal(input("Digite sua nota: "))
    if nota >= 0 and nota <= 10:
        soma += nota
        qtd += 1
    if nota == -1:
        break
media = soma / qtd

if media >= final:
    print("Voce está aprovado. Sua media foi de:", media)
else:
    print("Voce está reprovado. Sua media foi de:", media)
