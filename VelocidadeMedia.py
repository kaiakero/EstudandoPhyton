distancia = float(input('Informe a distancia total da viagem em quilometros:  '))
vel = float(input('informe a velocidade media em Km/h:  '))
velo = float(input('informe a velocidade da via:  '))
media = distancia/vel
print(f' o tempo total da viagem sera de {media:,.4f}hs')
if vel > 80 or vel>velo:
    print('voce esta andando acima da velocidade permitida nesta via')
elif vel<40:
    print('voce esta andando abaixo da velocidade minima desta via')
else:
    print('voce esta dentro da velocidade da via')
