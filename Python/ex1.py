def calcular_valores_investimento(valor_inicial, taxa_juros, anos):
    """
    Calcula o valor do investimento ao final de cada ano, considerando juros compostos

    Args:
    valor_inicial (float) O valor inicial do investimento.
    taxa_juros (float) A taxa de juros anual em percentual.
    anos (int) O número de anos do investimento.

    Return:
    list - Uma lista com o valor acumulado do investimento ao final de cada ano
    """
    valores_acumulados = []
    valor_atual = valor_inicial
    
    for ano in range(1, anos + 1):
        valor_atual *= (1 + taxa_juros / 100)
        valores_acumulados.append(valor_atual)
    
    return valores_acumulados

valor_inicial = float(input("Digite o valor inicial do investimento: "))
taxa_juros = float(input("Digite a taxa de juros anual (em %): "))
anos = int(input("Digite o número de anos: "))

valores = calcular_valores_investimento(valor_inicial, taxa_juros, anos)

print("\nValor acumulado ano a ano:")
for ano, valor in enumerate(valores, start=1):
    print(f"Ano {ano}: R$ {valor:.2f}")
