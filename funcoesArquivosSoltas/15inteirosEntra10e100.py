import random


def embaralha():

    numeros=[]

    for i in range(10):
        numeros.append(random.randint(10, 100))

    return numeros


print('10 números aleatorios entre 10 e 100.: %a' % embaralha())
