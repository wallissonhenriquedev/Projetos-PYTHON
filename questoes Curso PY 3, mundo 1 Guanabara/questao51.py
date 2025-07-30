n = 0

while n == 0:
    sexo = str(input("Qual seu sexo:[M/F] ")).upper()
    if sexo != "M" and sexo != "F":
        break
print ("Seu sexo é invalido.")
