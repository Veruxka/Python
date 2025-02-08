#Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário
#foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada km acima da velocidade permitida.

velocidade = int(input("Qual a velocidade o carro atingiu?"))
limite_velocidade = 80

if velocidade > limite_velocidade:
    excesso = velocidade - limite_velocidade
    multa = excesso * 5

    print(f"Você foi multado por ultapassar o limite de velocidade, a multa é de R${multa}")

else:

    print("Você está dentro do limite de velocidade")