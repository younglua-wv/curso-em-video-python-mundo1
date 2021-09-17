n = int(input("Informe um número: "))

uni = n // 1 % 10
dez = n // 10 % 10
cent = n // 100 % 10
mil = n // 1000 % 10

print(f"\nAnalisando o número {n}\n\nUnidade: {uni}\nDezena: {dez}\nCentena: {cent}\nMilhar: {mil}")