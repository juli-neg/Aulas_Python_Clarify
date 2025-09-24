from random import randint

print('###### Iniciando Jogo ######')

valorMinimo = 0
valorMaximo = 100
random = randint(valorMinimo, valorMaximo)
chute = 0
chances = 10


while chute != random:
    chute = input(f'Chute um numero entre {valorMinimo} a {valorMaximo}')
    if chute.isnumeric():
        chute = int(chute)
        chances -= 1
        if chute == random:
            print('----')
            print('Parabéns, você venceu! O número era {} e você ainda tinha {} chances.'.format(random, chances))
            print('----')
            break
        else:
            print('')
            if chute > random:
                print('Você ERROU! Dica: É um número menor.')
            else:
                print('Você ERROU! Dica: É um número maior.')   
            print(f'Você ainda possui {chances} chances') 
            print(' ')
        if chances == 0:
            print('')
            print('Suas chances acabaram, você errou. O número era {}'.format(random))
            print('')
            print('###### GAME OVER ######')
            break

