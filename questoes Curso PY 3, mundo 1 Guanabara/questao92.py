nome = input("Nome")
anodenascimento = int (input("Ano de nascimento"))
carteiradetrabalho = int (input("Carteira de trabalho(0 nao tem)"))
dicionario = {}
dicionario["nome"] = nome
dicionario["idade"] = 2025-anodenascimento

if carteiradetrabalho == 0:
    dicionario["ctps"] = "Nao tem"
elif carteiradetrabalho != 0:
    dicionario["ctps"] = "tem"
    anodecontratacao = int(input("ano de contratacao"))
    salario = float(input("Salario"))
    dicionario["ano de contratacao"] = anodecontratacao
    dicionario["salario"] = salario

for k, i in dicionario.items():
    print (f"{k} tem o valor {i}")