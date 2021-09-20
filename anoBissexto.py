from datetime import date

ano = int(input("Que ano quer analisar? (coloque '0' cas queira analisar o ano atual): "))

if ano == 0:
  ano = date.today().year

if ano % 400 == 0 and ano % 100 != 0 or ano % 4 == 0:
  print(f"O ano {ano} É um ano bissexto!")
else:
  print(f"O ano {ano} NÃO é um ano bissexto!")