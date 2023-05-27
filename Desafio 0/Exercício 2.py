def Encontrar_Menor_Diferenca():
    entrada = input("Digite os valores separados cada um por espaço ")
    #variavel entrada irá receber os valores inseridos quando o codigo for executado

    array = [int(x) for x in entrada.split()]
    #A função acima irá fazer com que o array seja dividido numero a numero pelos seus respectivos espaços em branco
    #e cada numero que seja dividido pelo seu espaço em branco será convertido em um numero inteiro e será alocado na variavel array
    array.sort()  # Ordena o array em ordem crescente

    menor = float('inf') #menor será a variavel para mostrar a menor diferença entre os valores foi inicializada com valor infinito
   
    pares = [] #lista pares inicializada com valor vazio

    for i in range(len(array) - 1):
        diferenca = abs(array[i] - array[i+1])  
        if diferenca < menor:
            menor = diferenca
# No primeiro for é realizado uma varredura para calcular a diferença dos valores de forma absoluta com a função 'abs', 
#isso será feito em cada par de numeros informados pelo usuário, e será realizada, 
#a diferença entre o valor do indice atual com o seu proximo no array como está na soma com i
#se a diferença absoluta for menor que 'menor' o valor menor será atualizado para a nova diferença

    for i in range(len(array) - 1):
        if abs(array[i] - array[i+1]) == menor:
            pares.append((array[i], array[i+1]))
#no segundo for ele irá percorrer novamente o array para ver quais pares possuem a menor diferença encontrada,
#e é adicionado a lista pares.

    return pares

r = Encontrar_Menor_Diferenca()
print(r)
#demonstração do resultado encontrado
