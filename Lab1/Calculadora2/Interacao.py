from Operacoes_Classes.subtrair import Subtrair as sub
from Operacoes_Classes.somar import Somar as som
from Operacoes_Classes.dividir import Dividir as d
from Operacoes_Classes.multiplicar import Multiplicar as m
from Operacoes_Classes.raiz import Raiz as r

class Interacao:
    def __init__(self):
        self.res: str = ''
        self.x: float = 0
        self.y: float = 0
        self.s: object

    def execute(self):
        '''
        A lógica está igual ao main2.py, a única mudança foi as abreviações dos imports
        '''
        print("Qual é o cálculo que quer efetuar? x + - / raiz")
        self.res:str = input()
        if self.res in "x+-/":
            print("Preciso que introduza dois valores:")
            self.x = float(input("x="))
            self.y = float(input("y="))
        elif self.res == "raiz":
            print("Preciso que introduza o valor:")
            self.x = float(input("x="))

        match self.res:
            case "+":
                s: som = som(self.x, self.y)
                res = s.get_resultado()
                print("O valor da operação somar é:", res)
            case "/":
                s: d = d(self.x, self.y)
                res = s.get_resultado()
                if type(res)==str:
                    print (res)
                else:
                    print("O valor da operação dividir é:", res)
            case "x":
                s: m = m(self.x, self.y)
                res = s.get_resultado()
                print("O valor da operação multiplicar é:", res)
            case "-":
                s: sub = sub(self.x, self.y)
                res = s.get_resultado()
                print("O valor da operação subtrair é:", res)

            case "raiz":
                s: r = r(self.x).get_resultado()
                print("O valor da raiz quadrada de", self.x, "é:", r(self.x).get_resultado())