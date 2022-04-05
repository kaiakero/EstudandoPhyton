rex = float(input('informe a posição de rex: '))
oli = float(input('informe a posição de oli: '))
bob = float(input('informe a posição de bob: '))
def teste(rex, oli, bob):

        distanciaRex = rex-oli
        if(rex<oli):
            distanciaRex = -rex+oli

        distanciaBob = bob-oli
        if(bob<oli):
            distanciaBob = -bob+oli

        if(distanciaRex == distanciaBob):
            print("Oli fugiu")
        elif(distanciaRex>distanciaBob):
            print("Bob chegou primeiro")
        else:
            print("Rex chegou primeiro")

teste(rex,oli,bob)
