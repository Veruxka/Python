#Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas. Ex:.
#Digite uma distância em metros:185.72
#A distância de 185.7m corresponde a:
#0.18572km        1857.2dm
#1.8572hm         18572.0cm
#18.572Dam        185720.0mm

distancia_metros = float(input("Digite uma distância em metros:"))

distancia_km = distancia_metros/1000
distancia_dm = distancia_metros *10
distancia_hm = distancia_metros /100
distancia_cm = distancia_metros *100
distancia_dam = distancia_metros /10
distancia_mm = distancia_metros *1000

print(f"A distância de {distancia_metros:}m corresponde a:")
print(f"{distancia_km: .5f} km")
print(f"{distancia_dm: .1f} dm")
print(f"{distancia_hm: .4f} hm")
print(f"{distancia_cm: .1f} cm")
print(f"{distancia_dam: .3f} dam")
print(f"{distancia_mm: .1f} mm")