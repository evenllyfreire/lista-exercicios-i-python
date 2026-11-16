# Questão 05 - Calculadora de Salário Líquido Simples
valor_hora = float(input("Valor da hora de trabalho: R$ ").replace(",", "."))
horas_trabalhadas = float(input("Horas trabalhadas no mês: ").replace(",", "."))

salario_bruto = valor_hora * horas_trabalhadas
inss = salario_bruto * 0.11                   # desconto fixo de 11%
salario_liquido = salario_bruto - inss

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto INSS (11%): R$ {inss:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
