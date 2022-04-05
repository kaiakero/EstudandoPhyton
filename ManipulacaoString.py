nome = (input('Informe seu nome completo?:  ').strip())

print (f'seu nome só em upper case é {nome.upper()}')
print (f'seu nome em lower case é {nome.lower()}')
print (f'your name have {len(nome) - nome.count(" ")} letters' )
lista = nome.split()
print (f'Olá {lista[0]}, seu primeiro nome tem {len(lista[0])}')