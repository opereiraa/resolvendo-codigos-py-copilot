#Descrição: Vamos testar se uma palavra é um palíndromo?! 
#Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

st = input('Digite o texto.: ')

st = st.replace(" ", "").lower()

if st == st[::-1]:
    print(f'O texto {st} é um palíndromo.')
else:
    print('O texto não é um palíndromo.')
