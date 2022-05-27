import numpy as np


def generate_crossword():
    return np.array(
        ['t', 'e', 's', 't', 'o', 'w', 'y',
         'a', 'ó', 'y', 'a', 't', 'r', 'p',
         't', 'e', 'r', 'i', 'f', 'z', 's',
         'r', 'a', 't', 'b', 'o', 'i', 'g',
         'y', 'i', 'n', 'm', 'o', 'z', 'u',
         'e', 'm', 'k', 'l', 'n', 'a', 'i']).reshape([6, 7])


print(generate_crossword())
