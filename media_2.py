#Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela.
#No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (Se ficou acima da média 7.0)

nome = (input("Qual é o seu nome?"))
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota"))
media = (nota1 + nota2) /2

if media >= 7.0:
    print(f"{nome} sua média é {media} e você teve um bom aproveitamento.")

else:
    print(f"{nome} sua média é {media} e você não teve um bom aproveitamento.")

