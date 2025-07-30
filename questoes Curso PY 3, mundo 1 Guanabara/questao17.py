from math import sqrt

cateto1 = float (input("Digite o cateto A: "))
cateto2 = float (input("Digite o cateto B: "))

hipotenusa = sqrt(cateto1**2+cateto2**2)

print (f"A hipotenusa é: {hipotenusa:.2f}")