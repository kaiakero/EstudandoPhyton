n1=float(input('Informe o valor de n1:  '))
n2=float(input('Informe o valor de n2:  '))
n3=float(input('Informe o valor de n3:  '))
if n1>=n2 and n1>=n3:
    print(f' o maior valor informado foi {n1}')
elif n2>=n1 and n2>=n3:
    print(f'O maior valor informado foi de {n2}')
else:
    print(f'O maior valor informado foi de {n3}')
if n1<=n2 and n1<=n3:
    print(f'O menor valor informado foi {n1}')
elif n2<=n1 and n2<=n3:
    print(f'O menor valor informado foi{n2}')
else:
    print(f'O menor valor informado foi {n3}')
