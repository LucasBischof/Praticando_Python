v1 = input('\033[1;31;42mDigite algo :\033[m')
print('\033[7;30;45mé um numero :\033[m',v1.isnumeric())
print('\033[4;33;47mé um palavra :\033[m',v1.isalpha())
print('\033[1;37;40mé um numero ou uma palavra :\033[m',v1.isalnum())
print('\033[0;34;41mé em maiusculo :\033[m',v1.isupper())
print('\033[4;32;43mé em minusculo :\033[m',v1.islower())