frase = "Curso em Video Python com Guanabara"

#Fatiamento

print(frase[4])
# Localiza a posição 4 da string
print(frase[:4])
# Vai do inicio até a posição 3
print(frase[4:])
# Vai da posição 4 até a última posição
print(frase[4::2])
# Começa na posição 4 até a posição 9 pulando de 2 em 2
print(frase[4:10]) 
# 4 = o até o 9 = V | Vai de um valor até outro menos 1 posição 
print(frase[4:21:2])
# Vai da posição 4 até a 20 pulando de 2 em 2

#----------------------------------------------------------------

#Análise

print(len(frase))
# Mostra a quantidade de caracteres da string
print(frase.count("o"))
# Conta quantas vezes aparece a letra na string
print(frase.count("o", 0, 13))
# Conta quantas vezes aparece a letra em um intervalo na string
print(frase.find("deo"))
# Conta quantas vezes ele encontrou "deo" na string
print(frase.find("Android"))
# Caso a palavra não exista na string ele retorna o valor -1
print("Curso" in frase)
# Mostra um True ou False se a palavra existir na string

#-----------------------------------------------------------------

# Transformação

print(frase.replace("Python", "Android"))
# Muda o valor x pelo valor y na string
print(frase.upper())
# Coloca todas as letras em caixa alta
print(frase.lower())
# Coloca todas as letras em minusculo
print(frase.capitalize())
# Coloca apenas a primeira letra da string em maiusculo
print(frase.title())
# Coloca todas as letras após um espaço em maiusculo

frase1 = "   Aprenda Python"

print(frase1.strip())
# Elimina os espaços excedentes no começo e no fim da string
print(frase1.rstrip())
