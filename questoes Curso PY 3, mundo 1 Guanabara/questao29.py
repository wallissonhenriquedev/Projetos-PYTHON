velocidade = int (input("Digite a velocidade do carro: "))

if velocidade >= 81:
    print (f"Voce foi multado! O valor da multa é de R${(velocidade-80)*7}")