def dividir(x: float, y: float) -> float:
    """
    Divide dois números
    :param x: valor dividendo
    :param y: valor divisor
    :return: retorna o resultado da divisão
    """
    try:
        return x / y
    except ZeroDivisionError:
        raise ZeroDivisionError("Erro: divisão por zero não é permitida")
