nota = float(input("Digite sua nota: "))
print('%.2f' % nota)
template_saida = '{:.2f}'
print(template_saida.format(nota))
print(f'{nota:.2f}')
