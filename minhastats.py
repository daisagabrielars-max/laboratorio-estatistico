def media(dados):
    return sum(dados) / len(dados)
def mediana(dados):
    ordenados = sorted(dados)
    n = len(ordenados)
    if n % 2 == 1:
        return ordenados[n // 2]
    else:
        return  (ordenados[n // 2 - 1] + ordenados[n // 2]) / 2
def amplitude(dados):
    return max(dados) - min(dados)   