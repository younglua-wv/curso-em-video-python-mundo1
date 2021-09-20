velocidade = int(input("Qual a velocidade atual do carro? "))

if velocidade <= 80:
  print("Tenha um bom dia!\nDirija com segurança!")

else:
  print(f"Você foi multado!\nVocê excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${float((velocidade - 80) * 7.0):.2f}\nTenha um bom dia!\nDirija com segurança!")