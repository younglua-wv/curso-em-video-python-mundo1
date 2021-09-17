nome = str(input("Digite seu nome completo: "))

print("Analisando seu nome...")

print(f"Seu nome em maiúsculas é: {nome.upper()}\nSeu nome em letras minúsculas é: {nome.lower()}")

dividido = nome.split()
primeiroNome = len(dividido[0])
totalDeCaracteres = len(nome) - nome.count(" ")

#print(nome.find(" "))

print(f"Seu nome tem ao todo {totalDeCaracteres} letras.")

print(f"Seu primeiro nome é {dividido[0]} e tem {primeiroNome} letras.")