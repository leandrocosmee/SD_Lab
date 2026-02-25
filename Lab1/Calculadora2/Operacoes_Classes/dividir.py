from typing import Union
class Dividir:
    def __init__(self, x:float, y:float):
        """Divide 2 numeros e guarda logo o resultado
        #Parametros:
            x (float): valor do numerador
            y (float): valor do divisor 
        """
        try:
            self.res: float = x / y
        except ZeroDivisionError:
            self.res = "error:dividing by zero"
    
    def get_resultado(self)->Union[float, str]:
        """Getter do resultado
        #return:
            resultado da divisão
        """
        return self.res
