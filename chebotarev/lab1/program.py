import numpy as np
import matplotlib.pyplot as plt
from function import Function


def draw_chart(func, range_, freq):
    temp = func.calculate(range_, freq)
    spectrum = func.spectrum()

    plt.subplot(2, 1, 1)
    plt.title(f'Сигнал {freq}Гц')
    plt.plot(temp[0], temp[1])
    plt.grid()

    plt.subplot(2, 1, 2).set_xticks(range(0, 50))
    plt.title(f'Частотный спектр сигнала {freq}Гц')
    plt.plot(spectrum[0], spectrum[1])
    plt.grid()
    
    plt.show()


def main():
    # sin = Function(np.sin)
    # draw_chart(sin, (0, 2), 1) # для 1 гц
    # draw_chart(sin, (0, 2), 2) # для 2 гц
    # draw_chart(sin, (0, 2), 4) # для 4 гц
    # draw_chart(sin, (0, 2), 8) # для 8 гц

    # cb = lambda x: np.sign(np.sin(x))
    # sing = Function(cb)
    # draw_chart(sing, (0, 2), 1) # для 1 гц
    # draw_chart(sing, (0, 2), 2) # для 2 гц
    # draw_chart(sing, (0, 2), 4) # для 4 гц
    # draw_chart(sing, (0, 2), 8) # для 8 гц
    

if __name__ == '__main__':
    main()