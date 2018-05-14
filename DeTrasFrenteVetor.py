palavra = 'ana'
cont = 1
pronto = []
x = int(len(palavra))-1
while cont <= len(palavra):
    pronto.append(palavra[x])
    cont += 1
    x -= 1
i = ''.join(pronto)
if i == palavra:
    print('Palindrome')
else:
    print('Não e palindrome')
print(''.join(pronto))
