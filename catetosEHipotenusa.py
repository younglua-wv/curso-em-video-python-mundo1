from math import hypot

co = float(input("Qual o comprimento do cateto oposto? "))
ca = float(input("Qual o comprimento do cateto adjacente? "))

print(f"A hipotenusa vai medir {hypot(co, ca):.2f}!")