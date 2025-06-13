def calculaTroco(troco, M):
  for moeda in M:
      if troco >= moeda:
          qtd = troco // moeda
          print(f"{qtd} moeda(s) de {moeda} centavo(s)")
          troco = troco % moeda
  if troco > 0:
      print(f"Troco restante não representável com as moedas disponíveis: {troco} centavos")

# Dicionário com as configurações
configuracoes = {
  1: [100, 50, 25, 10, 5, 2, 1],
  2: [100, 50, 20, 10, 5, 1],
  3: [100, 50, 20, 10, 5, 2, 1],
  4: [100, 50, 24, 12, 5, 1]
}

# Mostrar opções ao usuário
print("Escolha a configuração de moedas:")
print("1: Moedas de 1, 2, 5, 10, 25, 50 e 100 centavos")
print("2: Moedas de 1, 5, 10, 20, 50 e 100 centavos")
print("3: Moedas de 1, 2, 5, 10, 20, 50 e 100 centavos")
print("4: Moedas de 1, 5, 12, 24, 50 e 100 centavos")

# Leitura da configuração
opcao = int(input("Digite o número da configuração desejada (1 a 4): "))
if opcao not in configuracoes:
  print("Configuração inválida.")
  exit()

M = configuracoes[opcao]

# Leitura dos valores
valorCompra = float(input("Digite o valor da compra: R$ "))
valorPago = float(input("Digite o valor pago: R$ "))

# Converter para centavos
valorCompra = int(round(valorCompra * 100))
valorPago = int(round(valorPago * 100))
troco = valorPago - valorCompra

# Verificações
if troco < 0:
  print("Valor pago insuficiente.")
elif troco == 0:
  print("Não há troco.")
else:
  print(f"Troco: R$ {troco / 100:.2f}")
  calculaTroco(troco, M)
