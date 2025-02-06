#Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.

sal = float(input("Digite o salario do funcionário:"))
porcentagem = sal *15 /100 
novo_sal = sal + porcentagem
print(f"O salário do funcionário com 15% de aumento é R$ {novo_sal}")
