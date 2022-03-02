dist = float(input('Digite a distancia da viagem em km: '))

if dist<200:
    print('O valor da viagem sera {}R$'.format(dist*0.50))
else:
    print('O valor da viagem sera {}R$'.format(dist*0.45))
