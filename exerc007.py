n1 = int(input('\033[4;30;46mDigite o primeiro numero: \033[m'))
n2 = int(input('\033[7;30;46mDigite o segundo numero: \033[m'))
n3 = int(input('\033[37;40mDigite o terceiro numero: \033[m'))
s = n1 + n2 + n3
m = s/3
print('\033[36;41mA soma dos valores é {} e a media {:.2f}\033[m'.format(s,m))