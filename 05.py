nome = input('digite o nome do vendedor: ')
sala = float(input('digite o salario fixo de {} no mes:  '. format (nome)))
vendas = float(input('digite o valor total em reais vendidos por {} no mes:  '. format (nome)))
comissao = (vendas/100) *15
print ('o salario total de {} é de {}'. format (nome, sala+comissao))
