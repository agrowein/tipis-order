import math
import matplotlib.pyplot as plt
import numpy as np
import numpy.fft as fft
# Частота дискретизации - 10000гц
# Диапазон частот для сигнала ЧД/2 = 5000гц


# Расчет функции от времени
# cb - функция по которой высчитываются значения
# range_of_values - кортеж диапазона рассчета - (a, b)
# return - словарь с полями x и y. x и y - массивы
def culcFunc(cb, range, freq):
    values = dict()
    values['x'] = np.arange(range[0], range[1], 0.0001)
    values['y'] = cb(values['x'] * 2 * math.pi * freq)
    return values

# Функция отрисовки графика
# values - словарь со значениями x и y
# freq - частота
# title - строка(название графика)
def draw_charts(values, freq, title):
    plt.subplot(2, 1, 1)
    plt.plot(values['x'], values['y'])
    plt.grid()
    plt.title(f'Временное представление сигнала {title}')

    plt.subplot(2, 1, 2)
    plt.plot(freq['x'], freq['y'])
    plt.grid()
    plt.title(f'Частотный спектр сигнала {title}')
    plt.show()

# Рассчет значений и вызов отрисовки графиков
def initChart(f, cb):
    temp = culcFunc(cb, (0.0, 2.0), f) # рассчет значений сигнала во времени
    amp = np.abs(fft.fft(temp['y']))
    amp = amp[:len(amp) // 2] # Амплитуда частот на отсчетах
    freq = {'x':np.linspace(0, 5000, len(amp))[:100], 'y': amp[:100]} # Частотный спектр
    draw_charts(temp, freq, f'{f} Гц')


def main():
    f = lambda x: np.sign(np.sin(x))
    initChart(1, f) # Вычисления для 1Гц
    initChart(2, f) # Вычисления для 2Гц
    initChart(4, f) # Вычисления для 4Гц
    initChart(8, f) # Вычисления для 8Гц


if __name__ == '__main__':
    main()
