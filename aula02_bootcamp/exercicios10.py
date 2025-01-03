# 10) Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada
import math

raio = float(input("Digite o raio: "))

n1 = math.pi * (raio ** 2)

print(f"{n1:.2f}")

# :.2f -> formata o resultado para apresentar em 2 casas decimais