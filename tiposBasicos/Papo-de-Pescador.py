peso = float(input('Informe o peso: '))

aux = 0 
excesso = peso - 50

if excesso > 0:
    
    aux = excesso * 4
    
    print('Pague a multa: $%a reais' %aux)
else:
    print('Não foi multado')
