import matplotlib.pyplot as plt

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