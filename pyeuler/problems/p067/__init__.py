import os
from pyeuler.problems.p018 import main

if __name__ == '__main__':
    data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
    main(data_path)
