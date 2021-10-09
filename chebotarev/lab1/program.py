import numpy as np
from function import Function

def main():
    test = Function(np.sin)
    res = test.calculate((0, 1))
    print(res)
    

if __name__ == '__main__':
    main()