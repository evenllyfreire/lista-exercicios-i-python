# Questão 04 - Calculadora de Desconto em Compra
valor_total = float(input("Valor total do produto: R$ ").replace(",", "."))
percentual = float(input("Porcentagem de desconto (%): ").replace(",", "."))

desconto = valor_total * percentual / 100     # valor do desconto
preco_final = valor_total - desconto          # o que será pago

print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Preço final a pagar: R$ {preco_final:.2f}")
