classificacao = ("Cruzeiro", "Flamengo", "Red Bull Bragantino", "Bahia", "Palmeiras", "Botafogo", "Fluminense", "Atlético Mineiro", "Corinthians", "Ceará", "Mirassol", "Grêmio", "Santos", "Internacional", "Vasco", "São Paulo", "Fortaleza", "Juventude", "Vitória", "Sport")

print (f"Lista de times do brsileirao: {classificacao}\n\nOs 5 primeiros {classificacao[0:5]}\n\nOs 4 ultimos sao {classificacao[-4:]}\n\nOs 5 primeiros sao: Os times em ordem alfabetica {sorted(classificacao)}\n\nO Flamengo esta na {classificacao.index("Flamengo")+1} posicao")
