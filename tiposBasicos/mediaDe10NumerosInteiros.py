n = 1
aux = 0
while n <= 10:
    num = int(input('Digite o %a número: ' %n))
    aux = aux + num
    n += 1
n -= 1
aux = aux / n
print('O valor é ', aux )
