def maior(*num):
    cont = maior = 0
    print ("Analisando os valores...")
    for valor in num:
        print (f"valor {valor}")
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print (f"Foram informados {cont} valores, o maior valor é {maior}.")


maior (2, 4, 5, 6)