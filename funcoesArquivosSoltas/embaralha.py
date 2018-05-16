import random


def embaralha(entra):

    pronto = ''
    palavra = list(entra)
    random.shuffle(palavra)
    
    #Posso tirar essa linha e colocar direto no return
    pronto = ''.join(palavra)

    return pronto


entrada = input('Digite uma palavra: ')

print('Palavra pronta: %a' %embaralha(entrada))
