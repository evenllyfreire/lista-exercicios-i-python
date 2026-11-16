# Questão 01 - Exibe nome e salário
nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: R$ ").replace(",", "."))   # número float

print(f"Olá, {nome}! O seu salário é de R$ {salario:.2f}")
