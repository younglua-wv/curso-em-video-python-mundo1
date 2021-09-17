from math import trunc, ceil, floor

numero = float(input("Digite um valor: "))
print(f"O valor digitado foi {numero} e a sua porção inteira é {trunc(numero)}!\nAredondando para cima teremos a parte inteira de {ceil(numero)} e arredondando para baixo temos a parte inteira de {floor(numero)}!")