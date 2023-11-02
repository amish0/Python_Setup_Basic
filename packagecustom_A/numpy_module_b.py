import numpy as np

class NumpyMatrixManipulation:
    def __init__(self) -> None:
        self.version = np.__version__
        self.print_version()
    
    def print_version(self):
        print("numpy version: {}".format(self.version))
    
    def reshape_matrix(self, matrix, new_shape):
        return matrix.reshape(new_shape)
    
    def flatten_matrix(self, matrix):
        return matrix.flatten()
    
    def stack_matrices(self, matrix1, matrix2):
        return np.stack((matrix1, matrix2))
    
    def concatenate_matrices(self, matrix1, matrix2):
        return np.concatenate((matrix1, matrix2), axis=1)
    
    def split_matrix(self, matrix, axis):
        return np.split(matrix, axis, axis=1)
    
