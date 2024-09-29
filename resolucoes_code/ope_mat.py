# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

n1 = int(input('Digite o primeiro nº.: '))
n2 = int(input('Digite o segundo nº.: '))

opcao = input('Selecione a operação a ser realizada.: Soma (+), Subtração (-), Multiplicação (*) ou Divisão (/)')

if opcao == '+':
    print(n1+n2)
elif opcao == '-':
    print(n1-n2)
elif opcao == '*':
    print(n1*n2)
elif opcao == '/':
    print(n1/n2)
else:
    print('Opção inválida')