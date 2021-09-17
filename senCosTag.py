from math import radians, sin, cos, tan

angulo = int(input("Digite o ângulo que você deseja calcular: "))

print(f"O ângulo de {angulo}° tem o SENO de {sin(radians(angulo)):.2f}\n O ângulo de {angulo}° tem o COSSENO de {cos(radians(angulo)):.2f}\nO ângulo de {angulo}° tem a TANGENTE de {tan(radians(angulo)):.2f}! ")