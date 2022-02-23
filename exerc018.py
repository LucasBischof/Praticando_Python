import math
ang = int(input('Digite um angulo: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print('este angulo de {}° possui o cosseno {:.3f} seno {:.3f} e Tangente {:.3f}'.format(ang,c,s,t))