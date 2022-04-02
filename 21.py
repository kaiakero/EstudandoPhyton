import random
a1 = input('digite o nome do primeiro aluno:  ')
a2 = input('digite o nome do segundo aluno:  ')
a3 = input('digite o nome do terceiro aluno:  ')
a4 = input('digite o nome do quarto aluno:  ')
a5 = input('digite o nome do quinto aluno:  ')
lista = [a1,a2,a3,a4,a5]
random.shuffle(lista)
print(f'a ordem de apresentação sera{lista}')
