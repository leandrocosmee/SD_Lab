from Operacoes_Classes.subtrair import Subtrair 
from Operacoes_Classes.somar import Somar
from Operacoes_Classes.dividir import Dividir
from Operacoes_Classes.multiplicar import Multiplicar
from Operacoes_Classes.raiz import Raiz
from Interacao import Interacao as I

def main():
    """"Calculadora básica que pede ao utilizador o tipo de operação e 2 valores através de input()
    Não tem parâmetros nem returns
    """
    print("Qual é o cálculo que quer efetuar? x + - / raiz")
    res:str = input()
    if res in "x+-/":
        print("Preciso que introduza dois valores:")
        x: float = float(input("x=")) #float([algum valor]) força o valor inserido a ser float caso possível
        y: float = float(input("y="))
    elif res == "raiz":
        print("Preciso que introduza o valor:")
        x: float = float(input("x="))

    match res:
        case "+":
            s: Somar = Somar(x,y)
            res = s.get_resultado()
            print("O valor da operação somar é:", res)
        case "/":
            s: Dividir = Dividir(x,y)
            res = s.get_resultado()
            if type(res)==str:
                print (res)
            else:
                print("O valor da operação dividir é:", res)
        case "x":
            s: Multiplicar = Multiplicar(x,y)
            res = s.get_resultado()
            print("O valor da operação multiplicar é:", res)
        case "-":
            s: Subtrair = Subtrair(x,y)
            res = s.get_resultado()
            print("O valor da operação subtrair é:", res)

        case "raiz":
            s: Raiz = Raiz(x).get_resultado()
            print("O valor da raiz quadrada de", x, "é:", Raiz(x).get_resultado())

if __name__ == '__main__':
    main()
    interacao = I()
    interacao.execute()
