def maior_valor(num1, num2, num3):
    """
    Encontra o maior número entre três e retorna uma lista com eles ordenados

    Args:
    num1 (int | float) Primeiro número
    num2 (int | float) Segundo número
    num3 (int | float) Terceiro número

    Return:
    list - Uma lista com os três números em ordem crescente
    """
    maior = max(num1, num2, num3)
    
    print(f"O maior número é: {maior}")
    
    return sorted([num1, num2, num3])

resultado = maior_valor(10, 5, 8)
print(f"Números em ordem: {resultado}")
