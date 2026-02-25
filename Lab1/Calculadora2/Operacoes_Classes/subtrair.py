from typing import Union
class Subtrair:
    def __init__(self, x:float, y:float):
        """Faz a diferença de 2 numeros e guarda logo o resultado
        x (float): valor de um numero
        y (float): valor de um numero
        """
        try:    
            self.res: float = x - y
        except:
            self.res: str = "Valor inválido"
    
    def get_resultado(self)->float:
        """Getter do resultado
        :return: resultado da divisão
        """
        return self.res