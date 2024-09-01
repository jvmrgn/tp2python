def imprime_dados(*, nome, preco, quantidade):
    """
    Exibe os dados de um produto de forma organizada

    Args:
    nome (str) Nome do produto
    preco (float) Preço do produto
    quantidade (int) Quantidade em estoque do produto

    Return:
    None - A função apenas imprime os dados e não retorna nenhum valor
    """
    print("-----------------")
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Quantidade em estoque: {quantidade}")
    print("-----------------")

imprime_dados(nome="Notebook", preco=3500.00, quantidade=10)
imprime_dados(nome="PC Da Nasa", preco=1203120312.00, quantidade=3)
