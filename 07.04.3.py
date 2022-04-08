nome = str(input('digite seu nome:  ')).strip()
sexo = input('digite \'m\' para masculino e \'f\' para feminino:  ')
sexo=sexo.upper()
while sexo != 'F' or 'M':
    print('insira um genero valido')
    sexo = input('digite \'m\' para masculino e \'f\' para feminino:  ')
    sexo=sexo.upper()
if sexo == 'M':
    print(f'ola {nome}, seu sexo é masculino')
elif sexo =='F':
    print(f'ola {nome}, seu sexo é feminino')
    
