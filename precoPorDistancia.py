distancia = int(input("Qual a distância da sua viagem? "))

print(f"Você está prestes a começar uma viagem de {distancia}KM.")

if distancia <= 200:
  print(f"O preço da sua passagem será de R${distancia * 0.50:.2f}")
  
else:
  print(f"O preço da sua passagem será de R${distancia * 0.45:.2f}")