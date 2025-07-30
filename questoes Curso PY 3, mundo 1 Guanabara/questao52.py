import random

palpites = 1
n = random.randint(0,10)

while palpites >= 0:
    Acerta = int (input("Tente acertar o numero: "))
    if Acerta == n:
        break
    palpites += 1
print (f"Voce acertou! Com {palpites} tentativas.")