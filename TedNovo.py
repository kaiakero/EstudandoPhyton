nome = str(input    ('informe seu nome......: ')).strip()
altura = float(input('informe sua altura....: '))
peso = float(input  ('informe seu peso......: '))
idade = int(input   ('informe a sua idade...: '))
sexo = str(input    ('informe seu sexo (M/F): ')).strip().upper()
print(f'nome......: {nome}')
print(f'peso atual: {peso}')



if sexo == 'M':
    ideal = altura * 72.7 - 58
    teste = peso/ideal
    print(f'peso ideal: {ideal: .2f}')
    if teste > 1.05 :
        fit = peso - ideal
        print (f'{nome} Para chegar no seu peso ideal voce precisa perder {fit: .2f}KG')
    elif teste < 0.95:
        fit = ideal-peso
        print(f'{nome} para chegar no seu peso ideal voce precisa ganhar {fit: .2f}KG')
    else:
        print(f'{nome} voce esta no peso ideal')
elif sexo == 'F':
    ideal = altura * 62.1 - 44.7
    teste = peso/ideal
    print(f'peso ideal: {ideal: .2f}')
    if teste > 1.05 and teste:
        fit = peso - ideal
        print (f'{nome} para chegar no seu peso ideal voce precisa perder {fit: .2f}KG')
    elif teste < 0.95:
        fit = ideal-peso
        print(f'{nome} para chegar no seu peso ideal voce precisa ganhar {fit: .2f}KG')
    else:
        print(f'{nome}voce esta no peso ideal')    
if sexo == 'M' and idade > 65 :
   ideal = altura * 72.7 - 58
   teste = peso/ideal
   if teste > 1.2:
       x1 = peso * 100
       porc = (x1 / ideal)-100
       print(f'{nome} cuidado, voce deve procurar um medico pois esta {porc: .2f}% acima do seu peso')
elif sexo == 'F' and idade > 60:
   ideal = altura * 62.1 - 44.7
   teste = peso/ideal
   if teste > 1.2:
       x1 = peso * 100
       porc = (x1 / ideal)-100
       print(f'{nome} cuidado, voce deve procurar um medico pois esta {porc: .2f}% acida do seu peso')
