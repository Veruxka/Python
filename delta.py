#Desenvolva uma lógica que leia os valores de A, B e C de uma equação de segundo grau e mostre o valor de delta.
#Função para calcular valor de delta:
def calcular_delta(a, b, c):
    return b * b - 4*a*c

a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
c = int(input("Digite o terceiro valor:"))
#Fórmula de Delta: (B^2-4AC)
delta = calcular_delta(a, b, c)

print(f"O valor de Delta é {delta}")