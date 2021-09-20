frase = str(input("Digite uma frase: ")).upper().strip()

contador = frase.count("A")

primeiraOcorrencia = frase.find("A")+1

ultimaOcorrencia = frase.rfind("A")+1

print(f"A letra A aparece {contador} vezes na frase.\nA primeira letra A apareceu na posição {primeiraOcorrencia}\nA última letra A apareceu na posição {ultimaOcorrencia}")