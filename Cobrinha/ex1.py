def potencia(num, expoente=2):
    """
    Calcula a potência de um número conforme o expoente adicionado na função.

    Args:
    num (int | float) primeiro número, a base da potencia
    expoente (int | float ) O expoente em qual será calculado a potencia, o valor padrão é elevado ao quadrado.

    Return:
    (int | float) O resultado da potencia
    """
    return num ** expoente

resultado1 = potencia(3, 4)
print(f"3 elevado a 4 é: {resultado1}")

resultado2 = potencia(5)
print(f"5 elevado a 2 é: {resultado2}")
