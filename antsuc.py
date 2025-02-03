#Faça um programa que leia um número inteiro e mostre o seu antecessor e o seu sucessor.EX:.
#Digite um número: 9
#O antecessor de 9 é 8.
#O sucessor de 9 é 10.

num = int(input("Digite um número:"))
ant = num - 1
suc = num +1
print (f"O antecessor de {num} é {ant}.")
print (f"O sucessor de {num} é {suc}.")