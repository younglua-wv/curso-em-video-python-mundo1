print("-="*20)

print("Analisador de Triângulos")

print("-="*20)

seg_a = float(input("Qual o valor do primeiro segmento? "))
seg_b = float(input("Qual o valor do segundo segmento? "))
seg_c = float(input("Qual o valor do terceiro segmento? "))

if seg_a + seg_b > seg_c and seg_b + seg_c > seg_a and seg_a + seg_c > seg_b:
  print("Os segmentos acima PODEM FORMAR um triângulo!")
else:
  print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")