from Operacoes_Funcoes.dividir import dividir
from Operacoes_Funcoes.multiplicar import multiplicar
from Operacoes_Funcoes.somar import somar
from Operacoes_Funcoes.subtrair import subtrair
from Operacoes_Funcoes.raiz import raizquadrada

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
            print("O resultado da multiplicação é:", multiplicar(x, y))
        case "/":
            try:
                print("O resultado da divisão é:", dividir(10, 0))
            except ZeroDivisionError as e:
                print("Error:", e)
        case "+":
            print("O resultado da soma é:", somar(x, y))
        case "-":
            print("O resultado da subtração é:", subtrair(x, y))
        case "raiz":
            print("A raiz quadrada de", x, "é:", raizquadrada(x))

if __name__ == '__main__':
    main()