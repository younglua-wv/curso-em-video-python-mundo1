from random import randint
from time import sleep
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente Adivinhar...")
print("-=-" * 20)

n = randint(0,5)

numero = int(input("Em que número eu pensei? "))

print("PROCESSANDO...")
sleep(3)

if numero != n:
  print(f"Você errou e eu ganhei!\nPensei no número {n} e não no {numero}")

else:
  print("Parabéns, você ganhou! Uhuuul!!!")