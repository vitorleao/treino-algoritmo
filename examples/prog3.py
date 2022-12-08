a = [2 * i for i in range(100_000)]
b = [2 * i + 1 for i in range(100_000)]

def func(a, b):
    b = set(b)
    for i in a:
        if i in b:
            return True
    return False

func(a, b)
