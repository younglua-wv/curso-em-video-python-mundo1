valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))

if valor1 < valor2 and valor1 < valor3:
  print(f"O Menor valor digitado foi {valor1}")
elif valor2 < valor3 and valor2 < valor1:
  print(f"O Menor valor digitado foi {valor2}")
else:
  print(f"O Menor valor digitado foi {valor3}")

#-------------------------------------------------

if valor1 > valor2 and valor1 > valor3:
  print(f"O Maior valor digitado foi {valor1}")
elif valor2 > valor3 and valor2 > valor1:
  print(f"O Maior valor digitado foi {valor2}")
else:
  print(f"O Maior valor digitado foi {valor3}")