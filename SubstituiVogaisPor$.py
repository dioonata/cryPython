palavra = 'dioonata'

contador = 1
tamanho = len(palavra)
pronto = []
ponteiro = 0

while contador <= tamanho:
    if palavra[ponteiro] in 'aeiou':
        pronto.append('$')
    else:
        pronto.append(palavra[ponteiro])
    contador += 1
    ponteiro += 1
fim = ''.join(pronto)
print(pronto)
print(fim)
