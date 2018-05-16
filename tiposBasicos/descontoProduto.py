produto = float(input('Valor do produto: '))
desconto = float(input('Valor do desconto: '))
aux = produto - (produto * (desconto/100))
print('O valor do produto com o desconto: ', aux)
