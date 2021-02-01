#This program generates a random 3X3 matrix
import numpy as np

def matrix_gen():
    mat= np.random.randint(9,size=(3,3))
    return mat

print(matrix_gen())
