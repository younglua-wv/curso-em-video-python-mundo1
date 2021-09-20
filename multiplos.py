salario = float(input("Qual o salário do funcionário? R$"))

if salario >= 1250.00:
  salarioaum = (salario * (10/100)) + salario
  print(f"Quem ganhava R${salario:.2f} passa a ganhar R${salarioaum:.2f}!")
else:
  salarioaum = (salario * (15/100)) + salario
  print(f"Quem ganhava R${salario:.2f} passa a ganhar R${salarioaum:.2f}!")