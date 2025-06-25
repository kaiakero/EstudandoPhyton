def troco_minimo_guloso(configuracao, valor_troco):
  """
  Resolve o problema do troco mínimo usando algoritmo guloso.

  Args:
      configuracao (int): Número da configuração de moedas (1-4)
      valor_troco (float): Valor do troco em reais

  Returns:
      dict: Dicionário com quantidade de cada moeda e total
  """

  # Definindo as configurações de moedas (em centavos)
  configuracoes = {
      1: [100, 50, 25, 10, 5, 2, 1],
      2: [100, 50, 20, 10, 5, 1],
      3: [100, 50, 20, 10, 5, 2, 1],
      4: [100, 50, 24, 12, 5, 1]
  }

  if configuracao not in configuracoes:
      return {"erro": "Configuração inválida"}

  moedas = configuracoes[configuracao]
  troco_centavos = int(round(valor_troco * 100))  # Converte para centavos

  resultado = {}
  total_moedas = 0

  # Algoritmo guloso: sempre escolhe a maior moeda possível
  for moeda in moedas:
      if troco_centavos >= moeda:
          quantidade = troco_centavos // moeda
          resultado[moeda] = quantidade
          troco_centavos -= quantidade * moeda
          total_moedas += quantidade

  # Se ainda sobrou troco, não foi possível dar o troco exato
  if troco_centavos > 0:
      resultado["erro"] = f"Não foi possível dar troco exato. Sobrou {troco_centavos} centavos"

  resultado["total_moedas"] = total_moedas
  return resultado

def formatar_resultado(resultado, valor_troco, configuracao):
  """
  Formata o resultado de forma legível.
  """
  print(f"\n=== RESULTADO ===")
  print(f"Configuração: {configuracao}")
  print(f"Troco: R$ {valor_troco:.2f}")
  print(f"Moedas utilizadas:")

  if "erro" in resultado:
      print(f"ERRO: {resultado['erro']}")
      return

  for moeda, quantidade in resultado.items():
      if moeda != "total_moedas" and quantidade > 0:
          if moeda >= 100:
              print(f"  {quantidade} moeda(s) de R$ {moeda/100:.2f}")
          else:
              print(f"  {quantidade} moeda(s) de {moeda} centavos")

  print(f"Total de moedas: {resultado['total_moedas']}")

# Função principal para testar
def main():
  """
  Função principal para demonstrar o funcionamento do algoritmo.
  """

  # Exemplo do enunciado
  print("=== EXEMPLO DO ENUNCIADO ===")
  resultado = troco_minimo_guloso(1, 0.95)
  formatar_resultado(resultado, 0.95, 1)

  # Outros exemplos de teste
  exemplos = [
      (1, 1.37),  # Configuração 1, R$ 1,37
      (2, 0.67),  # Configuração 2, R$ 0,67
      (3, 0.89),  # Configuração 3, R$ 0,89
      (4, 0.43),  # Configuração 4, R$ 0,43
  ]

  print("\n" + "="*50)
  print("OUTROS EXEMPLOS DE TESTE")
  print("="*50)

  for config, valor in exemplos:
      resultado = troco_minimo_guloso(config, valor)
      formatar_resultado(resultado, valor, config)
      print("-" * 30)

# Função para testar uma configuração específica
def testar_configuracao():
  """
  Permite ao usuário testar uma configuração específica.
  """
  try:
      config = int(input("Digite a configuração (1-4): "))
      valor = float(input("Digite o valor do troco (ex: 0.95): "))

      resultado = troco_minimo_guloso(config, valor)
      formatar_resultado(resultado, valor, config)

  except ValueError:
      print("Erro: Digite valores válidos!")

if __name__ == "__main__":
  main()

  # Descomente a linha abaixo para testar interativamente
  # testar_configuracao()
