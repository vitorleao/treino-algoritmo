a = [2 * i for i in range(100_000)]
b = [2 * i + 1 for i in range(100_000)]

def func(a, b):
    tamanho_a = len(a)
    tamanho_b = len(b)
    posicao_a = 0
    posicao_b = 0
    valor_a = a[posicao_a]
    valor_b = b[posicao_b]
    while True:
        if valor_a == valor_b:
            return True
        if valor_a < valor_b:
            posicao_a += 1
            if posicao_a >= tamanho_a:
                return False
            valor_a = a[posicao_a]
        else:
            posicao_b += 1
            if posicao_b >= tamanho_b:
                return False
            valor_b = b[posicao_b]

func(a, b)
