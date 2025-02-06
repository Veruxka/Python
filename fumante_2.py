#Eu copiei esse código do chat gpt para comparar com o que eu fiz. O que eu fiz está em (fumante.py).
#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos
#anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá
#e exiba o total em dias.

# Função para calcular a perda de vida
def calcular_perda_de_vida(cigarros_por_dia, anos_fumando):
    # Cálculo da perda total em minutos
    minutos_perdidos = cigarros_por_dia  10  365 * anos_fumando
    # Convertendo minutos para dias
    dias_perdidos = minutos_perdidos / (60 * 24)
    return dias_perdidos

# Entrada de dados
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Quantos anos você já fumou? "))

# Cálculo da perda de vida
dias_perdidos = calcular_perda_de_vida(cigarros_por_dia, anos_fumando)

# Exibindo o resultado
print(f"Você perdeu aproximadamente {dias_perdidos:.2f} dias de vida devido ao fumo.")
