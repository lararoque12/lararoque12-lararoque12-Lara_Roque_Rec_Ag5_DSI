aparelho = input("Digite o nome do aparelho: ")
watts = float(input("Qual a potência em Watts: "))
tempo = float(input("Qual o tempo médio de uso: " ))

consumoMensal = (watts * tempo * 30) / 1000
valorFixo = (consumoMensal * 0.5)

print(aparelho)
print ("Consumo estimado: ", consumoMensal, " watts")
print ("O valor da sua conta é de R$", valorFixo)

