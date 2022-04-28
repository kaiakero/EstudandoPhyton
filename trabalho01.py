#Vitor de souza pinto
produto = int(input("informe o codigo do produto:  "))
quantidade = int(input("informe a quantidade que voce comprou desse produto"))
if produto == 24:
    valor = quantidade * 12.9
    print(f"  O valor total gasto na loja foi de R${valor: .2f}")
elif produto == 32:
    valor = quantidade * 3.5
    print(f"  O valor total gasto na loja foi de R${valor: .2f}")
elif produto == 46:
    valor = quantidade * 22
    print(f"  O valor total gasto na loja foi de R${valor: .2f}")
else:
    print(f"o codigo {produto} não é interpretado como um codigo válido")
