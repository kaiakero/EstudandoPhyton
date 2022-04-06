number = int(input('informe um numero, de 0 a 9999:  '))
u = number // 1 % 10
d  = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10
print(f'seu numero {number}, tem {m} milhares,\n {c} centenas\n {d} dezenas\n {u} unidades')