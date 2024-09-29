# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado. 

st = input('Digite um texto.: ')
num = int(input('Digite o nº de vezes que deseja repetir.: '))

i = 0
while i < num:
    print(st)
    i+=1