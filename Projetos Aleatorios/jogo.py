import random
pontosfinais = 0
palavrad = "esquizofrenia"
palavram = "mercado"
palavraf = "pato"


while True:
    menu = int (input("MENU\n1. Jogar\n2. Ver regras\n3. Sair\n4. Verificar pontos "))
    if menu == 1:
        nivel = int (input("Escolha o nivel de difuldade: \n 1. Dificil(30 pontos)\n2. Medio(20 pontos)\n3. Facil(10 pontos)"))
        if nivel == 1:
            pontos = 30
            print (f"Voce escolheu o nivel Dificil, e pode ganhar ate {pontos} pontos.")
        elif nivel == 2:
            pontos = 20
            print (f"Voce escolheu o nivel Medio, e pode ganhar ate {pontos} pontos.")
        elif nivel == 3:
            pontos = 10
            print (f"Voce escolheu o nivel Facil, e pode ganhar ate {pontos} pontos.")
        for c in range(3):
            if nivel == 1:
                tentando = str (input(f"Palavra embaralhada: {''.join(random.sample(palavrad, len(palavrad)))}\nTentativas[{c}/3]:")).lower().strip()
            if tentando == palavrad:
                print ("Acertou!!!")    
                pontosfinais += 30
                break
        if nivel == 2:
            tentando = str (input(f"Palavra embaralhada: {''.join(random.sample(palavrad, len(palavram)))}\nTentativas[{c}/3]:")).lower().strip()
            if tentando == palavram:
                print ("Acertou!!!")  
                pontosfinais += 20  
                break
        if nivel == 3:
            tentando = str (input(f"Palavra embaralhada: {''.join(random.sample(palavrad, len(palavraf)))}\nTentativas[{c}/3]:")).lower().strip()
            if tentando == palavraf:
                print ("Acertou!!!")    
                pontosfinais += 10
                break
            else: 
                print ("Voce errou! Execute o codigo para jogar novamente.")
    elif menu == 2:
        print ("OBJETIVO:\n\nO objetivo do jogo é adivinhar a palavra original a partir de sua versão embaralhada, com o jogador tendo 3 tentativas por palavra. O jogo possui três níveis de dificuldade: fácil, médio e difícil, com pontuação de 10, 20 e 30 pontos, respectivamente, por acerto. O jogador deve tentar acertar a palavra embaralhada em cada nível, sendo que, se errar 3 vezes, a palavra correta será revelada. As respostas do jogador são tratadas de forma que não importa o uso de maiúsculas ou espaços extras. Ao final, o jogo exibe a pontuação total do jogador, e ele pode escolher jogar novamente ou sair.")
    elif menu == 3:
        print ("Voce saiu do menu. Caso queira abrir denovo, execute o codigo novamente.")
        break
    elif menu == 4:
            print (f"Seus Pontos atual sao: {pontosfinais}")
    else:
        print ("Opcao Invalida.")