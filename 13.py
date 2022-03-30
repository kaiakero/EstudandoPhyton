import random
a1 = input('digite o nome do primeiro mascaradinho:  ')
a2 = input('digite o nome do segundo mascaradinho:  ')
a3 = input('digite o nome do terceiro mascaradinho:  ')
a4 = input('digite o nome do quarto mascaradinho:  ')
a5 = input('digite o nome do quinto mascaradinho:  ')
lista = [a1,a2,a3,a4,a5]
sorteio = random.choice(lista)
print (f'O cria do terceiro mais corta brisa é o {sorteio}')
