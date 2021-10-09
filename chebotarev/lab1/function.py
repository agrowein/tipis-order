import numpy as np

class Function: 
    '''
    Класс рассчитывает значения для переданной функции.
    '''

    def __init__(self, f): 
        self.f = f
        self.sampling_step = 0.0001 # шаг дискретизации 

    def calculate(self, range, freq=1):
        '''
        Метод рассчета значений функции от времени
        Args:
            range (tuple): Диапазон значений.
            freq (number, optioan): Частота. Defaults to 1.

        Returns:
            tuple: {x,y} массивы значений на диапазоне по X и Y
        '''
          
        x = np.arange(range[0], range[1], self.sampling_step)
        y = self.f(x * 2 * np.pi * freq)
        return (x, y)
        