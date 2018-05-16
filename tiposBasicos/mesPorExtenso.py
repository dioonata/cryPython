meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

dia, mes, ano = '13/1/1997'.split('/')

pronto = pronto = dia + '/' + meses[int(mes) - 1] + '/' + ano

print('Sua data de nascimento é: %s' %pronto)
