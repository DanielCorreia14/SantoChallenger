def lista_asteriscos(): #definição da lista
    #entrada de dados em N para saber até onde o for irá ser percorrido
    n = int(input("Insira o valor de n: "))


    lista = [] 
    #criação de lista vazia para alocar os asteriscos de acordo com o valor
    # de n que irá seguir a sequencia de preenchimento até o numero fornecido
    
    for i in range(1, n+1):
        #for que irá pegar o valor de N e limitar até ele e enquanto for percorrido irá adicionar a qtd de asteriscos
        #a variavel asteriscos, e apos isso será alocada na lista esse valor com o devido caminho do for
        asteriscos = '*' * i
        lista.append(asteriscos)
    return lista

resultado = lista_asteriscos()
print(resultado)
#variavel resultado será mostrado na tela após ter recebido o valor da lista definida
