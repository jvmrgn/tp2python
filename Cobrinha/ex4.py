def exibir_mensagem(mensagem, repeticoes=1):
    """
    Exibe uma mensagem um número especificado de vezes

    Args:
    mensagem (str) A mesnagem que será exibida
    repeticoes (int, opcional) O número de vezes que a mensagem será repetida. O valor padrão é 1

    Return:
    None - A função apenas imprime a mensagem e não retorna nenhum valor.
    """
    for _ in range(repeticoes):
        print(mensagem)

exibir_mensagem("Fala galera!!", 3)
exibir_mensagem("Bem vindo ao meu TP!!")
