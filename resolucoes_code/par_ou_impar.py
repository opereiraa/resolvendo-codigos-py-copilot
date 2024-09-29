#Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
#Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

num = int(input('Digite um número inteiro.: '))

resultado = num%2

if resultado > 0:
    print('O número é impar.')
else:
    print('O número é par.')