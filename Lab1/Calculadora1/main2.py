from Operacoes_Funcoes.dividir import dividir
from Operacoes_Funcoes.multiplicar import multiplicar
from Operacoes_Funcoes.somar import somar
from Operacoes_Funcoes.subtrair import subtrair
from Operacoes_Funcoes.raiz import raizquadrada

def main():
    """Pede 2 valores ao utilizador e faz todas as operações
    """
    x: float = float(input("x="))
    y: float = float(input("y="))

    print("O resultado da multiplicação é:", multiplicar(x, y))
    try:
        print("O resultado da divisão é:", dividir(x, y))
    except ZeroDivisionError as e:
        print("Error:", e)
    print("O resultado da soma é:", somar(x, y))
    print("O resultado da subtração é:", subtrair(x, y))
    print("A raiz quadrada de", x, "é:", raizquadrada(x))

if __name__ == '__main__':
    main()