nota = float(input("Digite sua nota: "))
print(nota + 0.5)


# nota += 0.5
# if nota > 10:
#     nota = 10
nota = min(nota + 0.5, 10)
# nota = max(nota - 0.5, 0)
nota = nota + 0.5 if nota + 0.5 > 10 else 10
nota_formatado = f'{nota:.2f}'
print(nota_formatado)
