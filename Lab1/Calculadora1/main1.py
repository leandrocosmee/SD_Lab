from math import sqrt

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

def multiplicar(x: float, y: float) -> float:
    """
    Multiplica dois números
    :param x: valor multiplicando
    :param y: valor multiplicador
    :return: retorna o resultado da multiplicação
    """
    return x * y

def raizquadrada( x: float) -> float:
    """
    Calcula a raiz quadrada de um número
    :param x: valor a calcular a raiz quadrada
    :return: retorna o resultado da raiz quadrada
"""
    if x >= 0:
        return sqrt(x)
    else:
        return "Erro: raiz quadrada de número negativo não é permitida"
    
def somar(x: float, y: float) -> float:
    """
    Soma dois números
    :param x: valor a somar
    :param y: valor a somar
    :return: retorna o resultado da soma
    """
    return x + y

def subtrair(x: float, y: float) -> float:
    """
    Subtrai dois números
    :param x: valor subtraido
    :param y: valor a subtrair
    :return: retorna o resultado da subtraçao
    """
    return x - y

def main():
    print("Qual é o cálculo que quer efetuar? x + - / raiz")
    res: str = input()
    if res in "x+-/":
        print("Preciso que introduza dois valores:")
        x: float = float(input("x="))
        y: float = float(input("y="))
    elif res == "raiz":
        print("Preciso que introduza o valor:")
        x: float = float(input("x="))

    match res:
        case "x":
            print("O resultado da multiplicação é:", float = multiplicar(x, y))
        case "/":
            try:
                print("O resultado da divisão é:", dividir(x, y))
            except ZeroDivisionError as e:
                print("Error:", e)
        case "+":
            print("O resultado da soma é:", float = somar(x, y))
        case "-":
            print("O resultado da subtração é:", float = subtrair(x, y))
        case "raiz":
            print("A raiz quadrada de", x, "é:", raizquadrada(x))

if __name__ == '__main__':
    main()
