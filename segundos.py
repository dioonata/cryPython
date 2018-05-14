dias = float(input('informe dias: '))
horas = float(input('informe horas: '))
minutos = float(input('informe minutos: '))
segundos = float(input('Informe segundos: '))

auxDias = dias * ( (24 * 60) * 60)
auxHoras = (horas * 60) * 60
auxMinutos = minutos * 60
totalSegundos = auxDias + auxHoras + auxMinutos + segundos
print('Total de segundos: ', totalSegundos)
