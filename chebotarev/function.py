import numpy as np
import numpy.fft as fft

class Function:
    '''
    Класс рассчитывает значения для переданной функции.
    '''
    def __init__(self, f): 
        self.f = f
        self.sampling_step = 0.0001 # шаг дискретизации 
        self.maxfreq = int(1 / (self.sampling_step * 2)) 
        self.values = None

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
        self.values = (x, y)
        return self.values

    def spectrum(self):
        '''
        Метод рассчета спектра функции

        Returns:
           tuple: {x,y} массивы значений на диапазоне по X и Y
        '''
        if not self.values:
            raise Exception('Значения функции не рассчитаны! \n Рассчитайте значения функции через метод calculate()')

        amplitude = np.abs(fft.fft(self.values[1]))
        amplitude = amplitude[:len(amplitude) // 2] 
        freq = (np.linspace(0, self.maxfreq, len(amplitude))[:50], amplitude[:50])
        return freq
        
    