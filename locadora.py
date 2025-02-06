#A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de km percorridos
#por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa
#R$ 90,00 por dia e R$ 0,20 por km rodado.

kmpercorridos = float(input("Quantos km foram percorridos?"))
dias = float(input("Por quantos dias o carro foi alugado?"))
total = (dias * 90) + (kmpercorridos * 0.20)
print(f"O total a pagar é R$ {total}")