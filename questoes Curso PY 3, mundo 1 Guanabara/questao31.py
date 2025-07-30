distancia = int (input("Digite a quantidade de km da viagem: "))

if distancia <= 200:
    print (f"O preco da passagem vai ser de R${distancia*0.50}")
else:
    print (f"O preco da passagem vai ser de R${distancia*0.40}")