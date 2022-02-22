n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
soma = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2
div_i = n1//n2
e = n1**n2
print('A soma é {} subtração {} e multiplicação {}'.format(soma,sub,mult), end=' ')
print('A divição {:.3f} ea intera é {} e a potencia {}'.format(div,div_i,e))