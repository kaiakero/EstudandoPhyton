frase = str(input('digite uma frase: ')).upper().strip()
print(f'a letra \"A\" aparece {frase.count("A")} vezes na frase')
print(f'a letra \"A\" aparece pela primeira vez na posição {frase.find("A")+1}')
print(f'a letra \"A\" aparece pela ultima vez na posição {frase.rfind("A")+1}')
