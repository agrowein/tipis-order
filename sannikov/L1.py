import numpy as np
import matplotlib.pyplot as plot

def main():
    analize(np.sin, (0, 10), 1)
    analize(np.sin, (0, 10), 2)
    analize(np.sin, (0, 10), 4)
    analize(np.sin, (0, 10), 8)

# Временное представление сигнала
def temp(f, range, freq):
    xval = np.arange(range[0], range[1], 0.0001)
    yval = []
    for x in xval: 
        yval.append(f(x * 2 * np.pi * freq))
    
    return (xval, yval)

# Расчет частотного спектра
def freq(signal):
    y = np.abs(np.fft.fft(signal))
    y = y[:len(y) // 2] 
    freq = (np.linspace(0, 5000, len(y))[:100], y[:100])
    return freq
    
# Функция анализа сигнала 
# Рассчитывает значения сигнала, его частотного спектра и визуализирует его
def analize(f, range, frequency=1):
    temp_res = temp(f, range, frequency)
    spectrum = freq(temp_res[1])

    add_chart(temp_res, f'Гармонический сигнал {frequency} Гц', 1, ('Время, с', 'Сигнал'))
    add_chart(spectrum, f'Частотный спектр сигнала {frequency} Гц', 2, ('Частота, Гц', 'Отсчеты'))
    
    plot.show()

#Функция добавляет график в окно визулизации 
def add_chart(values, title, i, labels):
    plot.subplot(2, 1, i)
    plot.title(title)
    plot.grid()
    plot.xlabel(labels[0])
    plot.ylabel(labels[1])
    plot.plot(values[0], values[1])

if __name__ == '__main__':
    main()