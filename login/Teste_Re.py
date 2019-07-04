import re

lista = ['Gilmar gosta de jogar video game','tosato','Gilmar']
totalizador = 0
for m in range(len(lista)):
    nome_pes = re.search(r'^Gilmar',lista[m])
    if  nome_pes != None:
        totalizador += 1

print('Total encontrado : ', totalizador)