numeros = []
n1 = int(input('informe o valor de n1: '))
n2 = int(input('informe o valor de n2: '))
n3 = int(input('informe o valor de n3: '))
numeros.append(n1)
numeros.append(n2)
numeros.append(n3)
ord = sorted(numeros)
n1 = ord[0]
n2 = ord[1]
n3 = ord[2]
print(f'{n1}\n{n2}\n{n3}')
