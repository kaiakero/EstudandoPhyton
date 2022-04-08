nome = input('informe seu nome')
sexo = str(input('informe seu sexo:  ')).upper()
idade = int(input('informe a sua idade:  '))
if idade>18 and sexo == 'MASCULINO':
    print(f'{nome}, voce é adulto')
elif idade<18 and sexo =='MASCULINO':
    print(f'{nome}, voce nao é adulto')
elif idade >21 and sexo =='FEMININO':
    print(f'{nome} voce não é adulta')
else:
    print(f'{nome} voce não é adulta')
    
