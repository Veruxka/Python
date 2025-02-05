#Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostra quantos dólares ela pode comprar.
# Considere U$1,00 = R$5,76.

dinheiro = float(input("Quanto dinheiro você tem na carteira?"))
cotacao_dolar = float (5.76)
dinheiro = dinheiro * cotacao_dolar

print(f"Você pode comprar U$ {dinheiro}")