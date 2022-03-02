veloc = float(input('Digite a velocidade do seu carro: '))
multa = float(-7*(80-veloc))
if veloc>80:
    print('Voce esta multado no valor de {:.2f}R$'.format(multa))
else:
    print('Muito bem, esta na velicidade permitida')