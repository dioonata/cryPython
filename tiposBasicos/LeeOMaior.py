a = int(input('Informe o 1 número: '))
b = int(input('Informe o 2 número: '))
c = int(input('Informe o 3 número: '))

if a >= b and a >= c:
    print('O primeiro número é maior')
elif b >= c:
    print('O primeiro número é maior')
else:
    print('O terceiro número é o maior')
