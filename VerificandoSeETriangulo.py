a = float(input('Informe o primeiro lado do triângulo: '))
b = float(input('Informe o segundo lado do triângulo : '))
c = float(input('Informe o terceito lado do triângulo: '))

if a < b + c or b < a + c or c < a + b:
    if a == b == c:
        print('Equilátero')
    elif a == b or b == c or a == c:
        print('Isósceles')
    else:
        print('Escaleno')
    
else:
    print('Isso nâo pode ser um triângulo!')
    print('Um dos lados e maior que a soma do outro!')

