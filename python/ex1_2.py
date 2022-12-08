from decimal import Decimal, getcontext

getcontext().prec = 3
nota = Decimal(input("Digite sua nota: "))
nota += Decimal('0.5')
print(nota)

1 / 2 = 0.5
0.5 / 2 = 0.25
0.25 / 2 = 0.125

0.1
0.2

(0.1 + 0.2) + 0.3 != 0.1 + (0.2 + 0.3) != 0.2 + 0.1 + 0.3