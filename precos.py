p1=float(input('Informe o valor do primeiro produto:  '))
p2=float(input('Informe o valor do segundo produto:  '))
p3=float(input('Informe o valor do terceira produto:  '))
if p1==p2 and p2==p3:
   print('os valores dos produtos são todos iguais ')
elif p1>=p2 and p2>=p3:
   print(f'os produtos em ordem decrescente de preço custam: R${p1}, R${p2} e R${p3}')
elif p2>=p1 and p1>=p3:
   print(f'os produtos em ordem decrescente de preço custam: R${p2}, R${p1} e R${p3}')
elif p1>=p3 and p3>=p2:
   print(f'os produtos em ordem decrescente de preço custam: R${p1}, R${p3} e R${p2}')
elif p2>=p3 and p3>=p1:
   print(f'os produtos em ordem decrescente de preço custam: R${p2}, R${p3} e R${p1}')
elif p3>=p1 and p1>=p2:
   print(f'os produtos em ordem decrescente de preço custam: R${p3}, R${p1} e R${p2}')
elif p3>=p2 and p2>=p1:
   print(f'os produtos em ordem decrescente de preço custam: R${p3}, R${p2} e R${p1}')
