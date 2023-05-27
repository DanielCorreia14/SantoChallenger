def encontrar_sub():
    entrada = input("insira numeros inteiros separados por espaço ")
    #input para receber os valores pelo usuário
    num = [int(x) for x in entrada.split()]
    #split para dividir a string em numeros inteiros quando forem inseridos espaçadamente e alocados na variavel num
    
    sub = [[]]
    #sub é inicializada com uma lista contendo um subconjunto vazio, lista vazia e dentro de outra lista vazia
    for n in num:
        #for para percorrer cada numero inserido pelo usuário e para cada numero será gerado subconjuntos 
        sub += [subset + [n] for subset in sub]

    return sub

r = encontrar_sub()
print(r)
#demonstração do resultado encontrado
