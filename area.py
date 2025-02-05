#Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta
#necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2m².

larg = float(input("Digite a largura da parede:"))
alt = float(input("Digite a altura da parede:"))
area = larg * alt 
tinta = area / 2
print(f"Será necessário {tinta} litros de tinta para pintar a área de {area} metros²")