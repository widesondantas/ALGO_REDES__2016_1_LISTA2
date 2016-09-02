#QUALIDADE DE FILMES
ALGORITMOS

contador_regular = 0
contador_bom = 0
contador_otimo = 0

PARA i de 0 ate faca

ESCREVA " Insira a sua opniao: ótimo – 3, bom – 2, regular – 1: "
LEIA opniao

    se opniao = 1:
        contador_regular = contador_regular + 1

    se opniao = 2:
        contador_bom = contador_bom + 1

    se opniao = 3:
        contador_otimo = contador_otimo + 1

    senao
        ESCREVA 'Opção Invalida'

ESCREVA 'A quantidade de pessoas que responderam ótimo: ' , contador_otimo
ESCREVA 'A quantidade de pessoas que responderam bom: ' , contador_bom
ESCREVA 'A quantidade de pessoas que responderam regular: ' , contador_regular

FIM_ALGORITMOS