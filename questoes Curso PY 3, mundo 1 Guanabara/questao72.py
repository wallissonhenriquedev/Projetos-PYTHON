nums = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "(dezoito)", "dezenove", "vinte")

n = int(input("Digite um numero entre 0 e 20: "))
while True:
    if n >= 0 and n <= 20:
        print (f"Voce digitou o numero {nums[n]}")
    else:
        n = input("Tente novamente, Digite um numero entre 0 e 20: ")
    cont = int(input("Quer continuar? [1] Sim, [2] Nao "))
    if cont == 1:
        n = int(input("Digite um numero entre 0 e 20: "))
    else:
        print ("Terminamos")
        break