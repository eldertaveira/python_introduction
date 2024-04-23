def fazer_pizza(tamanho, *topicos):
    """Exibe a lista de ingredientes pedidos."""
    print(f"Sua pizza tamanho {tamanho} será feita com: ")
    for item in topicos:
        print('- ' + item)