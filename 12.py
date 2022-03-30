import math
angulo = float(input('informe um ângulo:  '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print (f'O seno de {angulo} ° equivale a {seno: ,.2f}')
print (f'O cosseno de {angulo} ° equivale a {cos: ,.2f}')
print (f'A tangente de {angulo} ° equivale a {tan: ,.2f}')
