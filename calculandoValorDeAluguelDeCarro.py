dias = float(input("Por quantos dias você alugou o carro? "))
kmRodados = float(input("Quantos KM você rodou? ")
valorPorDias = dias * 60
valorPorKm = kmRodados * 0.15
print(f"O valor para o aluguel de um carro por {dias} dias e {kmRodados}KM rodados é de R${valorPorDias + valorPorKm:.2f}.")