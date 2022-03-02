sal = float(input('Digite seu salario:R$'))
if sal>1250:
    print('O seu aumento é de 10% seu salario sera R${:.2f}'.format(sal*1.1))
else:
    print('O seu aumento é de 15% seu salario sera R${:.2f}'.format(sal*1.15))
