tamanho = int(input('Informe o tamanho em metros quadrados da aréa a ser pintada: '))
lataLitros = 18
qtdMetrosLata = lataLitros * 3
custoLata = 80

totalDeLatas = tamanho / qtdMetrosLata
round (totalDeLatas)
total = totalDeLatas * 80

print('O total a ser pago vai ser: R$', total) 
print('Total de latas: ', round(totalDeLatas))
