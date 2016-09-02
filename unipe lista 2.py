
print ('Digite as suas 3 notas')

n1 = float(input("Digite sua primeira nota: "))

n2 = float(input("Digite sua segunda nota: "))

n3 = float(input("Digite sua terceira nota: "))

media = (n1+n2+n3)/3

if media <=4:
    print("Reprovado")
elif media >=4 and media <7:
    print("Prova Final")
else:
    print("Aprovado")

