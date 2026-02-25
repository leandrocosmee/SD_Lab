from Operacoes_Classes.dividir import Dividir
from Operacoes_Classes.multiplicar import Multiplicar
from Operacoes_Classes.somar import Somar
from Operacoes_Classes.subtrair import Subtrair
from Operacoes_Classes.raiz import Raiz

def main():
    """Pede 2 valores ao utilizador e faz todas as operações
    """
    x: float = float(input("x="))
    y: float = float(input("y="))

    print("O resultado da multiplicação é:", Multiplicar(x, y).get_resultado())
    try:
        print("O resultado da divisão é:", Dividir(x, y).get_resultado())
    except ZeroDivisionError as e:
        print("Error:", e)
    print("O resultado da soma é:", Somar(x, y).get_resultado())
    print("O resultado da subtração é:", Subtrair(x, y).get_resultado())
    print("A raiz quadrada de", x, "é:", Raiz(x).get_resultado())

if __name__ == '__main__':
    main()