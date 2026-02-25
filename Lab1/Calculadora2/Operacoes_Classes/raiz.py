from typing import Union
from math import sqrt
class Raiz:
    def __init__(self, x:float):
        """Calcula a raiz de um numero
        #Parametro:
        x (float): numero a ser operado a raiz        
        """
        if x < 0:
            self.res = "error:negative number"
        else:
            self.res: float = sqrt(x)

    def get_resultado(self)->float:
        """Getter do resultado
        #return:
            resultado da divisão
        """
        return self.res
    