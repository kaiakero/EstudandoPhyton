#vitor de souza pinto
nome = str(input('informe seu nome: ')).strip()
n1 = float(input("Informe a nota obtida na primeira prova: "))
n2 = float(input("Informe a nota obtida na segunda prova: "))
media = (n1+n2)/2
if media < 4:
    print("Reprovado por media")
elif media >=8:
    print("Aprovado por média")
else:
    exame = float(input("Informe a nota obtida no exame: "))
    if exame > n1 or exame > n2:
        if n1<=n2:
            #menor = n1
            n1 = exame
            m2 = (n1+n2)/2
            if m2>=6:
                print(f"{nome} voce foi aprovado apos exame")
            else]:
                print(f"{nome} voce foi reprovado apos exame")
        else:
            #menor = n2
            n2 = exame
            m3 = (n1+n2)/2
            if m3>=6:
                print(f"{nome} voce foi aprovado apos exame")
            else:
                print(f"{nome} voce foi reprovado apos exame")
    else:
                print(f"{nome} voce foi reprovado apos exame")
