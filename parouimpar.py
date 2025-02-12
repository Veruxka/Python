#Desenvolva um programa que leia um número inteiro e mostre se ele é par ou impar.
#Para saber se um número é par ou ímpar temos que saber se ele é divisível por 2 com resto 0.
#Se for, ele é par, senão é impar.

numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")


