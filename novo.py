#inicialição dos contadores
contador_regular = 0
contador_bom = 0
contador_otimo = 0

for i in range(10):

    opiniao = int(input('Digite sua opiniao sobre o filme: '))

    if opiniao == 1: #REGULAR
        contador_regular = contador_regular + 1

    elif opiniao == 2: # BOM
        contador_bom = contador_bom + 1

    else:# OTIMO
        contador_otimo = contador_otimo + 1

print("Qtd de opiniao em regular = %d" % contador_regular)
print("Qtd de opiniao em bom = %d" % contador_bom)
print("Qtd de opiniao em otimo = %d" % contador_otimo)


