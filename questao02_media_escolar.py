# Questão 02 - Calculadora de Média Escolar
nome = input("Nome do aluno: ")
nota1 = float(input("Nota 1: ").replace(",", "."))
nota2 = float(input("Nota 2: ").replace(",", "."))
nota3 = float(input("Nota 3: ").replace(",", "."))

media = (nota1 + nota2 + nota3) / 3      # média aritmética
print(f"A média do aluno {nome} é: {media:.2f}")
