lar = float(input('Digite a largura da sua parede:'))
alt = float(input('Digite a altura da sua parede'))
area = lar*alt
tin = area/2
print('Sua parede tem a dimensão de {}x{} e a sua area é de {}m².'.format(lar,alt,area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tin))