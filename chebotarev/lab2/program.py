import sys
sys.path.insert(0, "./../")

import numpy as np
from function import Function
from drawer import draw_chart

def main():
    cb = lambda x: np.sign(np.sin(x))
    sing = Function(cb)
    draw_chart(sing, (0, 2), 1) # для 1 гц
    draw_chart(sing, (0, 2), 2) # для 2 гц
    draw_chart(sing, (0, 2), 4) # для 4 гц
    draw_chart(sing, (0, 2), 8) # для 8 гц

if __name__ == '__main__':
    main()