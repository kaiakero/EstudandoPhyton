c1 = float(input('informe a medida em Cm do cateto oposto:  '))
c2 = float(input('informe em Cm a medida do cateto adjacente:  '))
hipo = (c1**2 + c2**2)**0.5
print(f'A medida da hipotenusa é de {hipo: ,.2f}Cm')


import math
ca = float(input('informe em Cm a medida do cateto adjacente:  '))
co = float(input('informe a medida em Cm do cateto oposto:  '))
hypot = math.hypot(ca,co)
print (f'A medida da hipotenusa é de{hypot: ,.2f}Cm') 
