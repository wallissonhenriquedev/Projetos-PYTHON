print ("=== Bem-vindo ao RPG de Texto! ===\n\n")
nome = input("Digite o nome do seu heroi: ")


while True:
    classe = int (input("Escolha sua classe:\n1 - Guerreiro (mais vida)\n2 - Mago (mais dano)\n3 - Arqueiro (mais critico)\nDigite o numero da sua classe: "))
    if classe == 1:
        Vida = 130
        dano = 10
        critico = 10
        classe = "Guerreiro"
        print (f"Personagem criado: {nome} - Classe: {classe}.\nVida: ")
        break
    elif classe == 2:
        Vida = 100
        dano = 30
        critico = 10
        classe = "Mago"
        print (f"Personagem criado: {nome} - Classe: {classe}.\nVida: ")
        break
    elif classe == 3:
        Vida = 100
        dano = 10
        critico = 30
        classe = "Arqueiro"
        print (f"Personagem criado: {nome} - Classe: {classe}.\nVida: ")
        break
    else: 
        print ("Heroi invalido.")
# acoes
defender = 5

# monstros
vidadomonstro = 100

while True: # Jogo rodando (eu que fiz essa bomba, nao e chat gpt)
    print ("Um monstro desconhecido apareceu!")
    acao = int (input("Oque deseja fazer?\n1 - Atacar\n2 - Defender\n3 - Fugir\nEscolha: "))
    if acao == 1:
        vidadomonstro -=dano
        print (f"Voce atacou! causou {dano} de dano. vida do monstro: {vidadomonstro}")
    elif acao == 2:
        vidadomonstro = vidadomonstro-defender
        print (f"Voce se defendeu! e conseguio causar {defender} de dano no monstro.")
    elif acao == 3:
        vida = vida-40
        print (f"Voce correu! se deu mal e perdeu 40 de vida.")
    else:
        print ("Acao invalida!")
if vidadomonstro == 0:
    print ("Voce derrotou o monstro! Parabens, {nome}!")
    
elif vida == 0: 
    print ("Voce foi derrotado! tente novamente")
    
