def gerar_lista_pares(n):
    """
    Gera uma lista contendo todos os números pares de 0 até o numero

    Args:
    n (int) O número limite até o qual serão gerados os números pares

    Return:
    list - Uma lista com todos os números pares de 0 até o numero
    """
    lista_pares = []
    for i in range(0, n + 1):
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares

num = int(input("Digite um número: "))
resultado = gerar_lista_pares(num)
print(f"Números pares de 0 até {num}: {resultado}")
