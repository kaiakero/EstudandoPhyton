import datetime
tempo = float(input('digite em segundos, o tempo total do evento:  '))
convert = str(datetime.timedelta(seconds = tempo))
print(f'o tempo do processo foi de {convert}')
