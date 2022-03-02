

import random2

num = random2.randint(0,5)
chute = int(input('Eu estou pensando em um numero de 0 a 5 tente adivinhar? '))
if num == chute:
    print('Ganhou eu pensei em {}'.format(num))
else:
    print('perdeu eu pensei em {}'.format(num))
