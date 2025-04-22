hora: int
hora = int(input("Digite um horário do dia ou da noite:"))
if hora < 12:
    print ("Bom dia!")
elif hora < 18:
    print ("Boa tarde!")
else: 
    print ("Boa noite!")
           
