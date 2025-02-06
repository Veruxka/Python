#Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas
#por dia e ganha R$ 25 por hora trabalhada.

dias = int(input("Quantos dias o funcionário trabalhou?"))
salario = dias * (8*25)
print (f"O salário deste mês é R${salario}")