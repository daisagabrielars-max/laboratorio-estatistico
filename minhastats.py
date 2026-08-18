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
def moda(dados):
    contagem = {}
    for v in dados:
        if v in contagem:
            contagem[v] = contagem[v] + 1
        else:
            contagem[v] = 1
    maior = max(contagem.values())
    modas = []
    for valor in contagem:
        if contagem[valor] == maior:
            modas.append(valor)
    return modas
def variancia(dados, amostral=True):
    m = media(dados)
    n = len(dados)
    soma = 0
    for x in dados:
                soma += (x - m) ** 2
    if amostral:
        return soma / (n - 1)
    else:
        return soma / n
def desvio_padrao(dados, amostral=True):
        return variancia(dados, amostral) ** 0.5