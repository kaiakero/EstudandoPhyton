import datetime
tempo = float(input('digite em segundos, o tempo total do evento'))
convert = str(datetime.timedelta(seconds = tempo))
print(convert)
