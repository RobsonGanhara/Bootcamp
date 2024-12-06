# 1) Solicite ao usuário que digite o seu nome
nome = input("Digite seu nome: ")

# 2) Solicite ao usuário que digite o valor do seu salário
salario = float(input("Digite seu salario: "))

# 3) Solicite ao usuário que digite o do bônus recebido
bonus = float(input("Digite a porcentagem do bonus recebido: "))

# 4) Calcule o valor do bonus final
kpi = (1000 + salario * bonus)

# 5) Imprima o cálculo do KPI para o usuário
print(f"{nome}, o valor do seu bonus final é {kpi}")

# 6) Imprima a mensagem personalizada incluindo o nome do usuário
print(f"Parabéns {nome}! Seu bonus final foi de {kpi + salario}")