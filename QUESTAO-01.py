#contadores
contador_regular = 0
contador_bom = 0
contador_otimo = 0

for i in range(10):
    opniao = int(input(" Insira a sua opniao: ótimo – 3, bom – 2, regular – 1: "))

    if opniao == 1:
        contador_regular = contador_regular +1

    if opniao == 2:
        contador_bom = contador_bom  + 1

    if opniao == 3:
        contador_otimo = contador_otimo +1

    else:
        print('Opção Invalida')
print('A quantidade de pessoas que responderam ótimo: ' %contador_otimo)
print('A quantidade de pessoas que responderam bom: ' %contador_bom)
print('A quantidade de pessoas que responderam regular: ' %contador_regular)