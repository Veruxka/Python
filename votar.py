#Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou nao votar.

idade = int(input("Qual é a sua idade?"))
idade_para_votar = 18
if idade > idade_para_votar:
    apto = idade > idade_para_votar
    print(f"Você está apto para votar.")

else:
    print("Você está inapto para votar.")