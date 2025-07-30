from time import sleep

def contagem(i=0,f=0,p=1):
    print ("-="*20)
    print (f"contagem de {i} ate {f} de {p} em {p}")
    sleep(1.5)
    if passo < 0:
        p = abs(passo)
    elif passo == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print (f"{cont}", end = " ")
            cont += p 
        print ("FIM!")
    else:
        cont = i
        while cont >= f:
            print (f"{cont}", end = " ")
            cont -= p 
        print ("FIM!")

inicio = int(input("Digite  o inicio "))
fim = int(input("Digite  o fim "))
passo = int(input("Digite  o passo "))
contagem(inicio, fim, passo)