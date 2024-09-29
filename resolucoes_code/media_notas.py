#Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. 
#Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

notas = []
i = 0
while i < 3:
    num = int(input(f'Digite sua nota {i+1}.:'))
    notas.append(num)
    i+=1

print(f'A média é de.: {round(sum(notas)/len(notas),2)}')