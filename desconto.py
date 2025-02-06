#Crie um programa que leia o preço de um produto, calcule e mostre o seu preço promocional, com 5% de desconto.

preço = float(input("Digite o preço do produto:"))
desconto = preço * 5 / 100 
valor_final = preço - desconto
print(f"O valor do produto com desconto de 5% é {valor_final}")