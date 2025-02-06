#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos
#anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá
#e exiba o total em dias.

quant = int(input("Quantos cigarros você fuma por dia?"))
anos = int(input("Por quantos anos você fumou?"))
minutos_dia = 1440
ano_1 = 365
dias_de_vida =  anos * ano_1 * quant / minutos_dia 
print(f"Você perderá {dias_de_vida:.0f} dias de vida.")