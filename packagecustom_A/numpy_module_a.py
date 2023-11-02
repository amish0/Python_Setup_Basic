# numpy basic operations
import numpy as np

class NumpyMatrixInitializer:
    def __init__(self):
        self.version = np.__version__
        self.print_version()
    
    def print_version(self):
        print("numpy version: {}".format(self.version))
    
    def create_array(self):
        self.array = np.array([1,2,3,4,5])
    
    def create_matrix(self):
        self.matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
    
    def create_zeros(self):
        self.zeros = np.zeros((3,3))
    
    def create_ones(self):
        self.ones = np.ones((3,3))
    
    def create_identity(self):
        self.identity = np.identity(3)
    
    def create_random(self):
        self.random = np.random.random((3,3))
    
    def create_arange(self):
        self.arange = np.arange(0, 10, 2)
    
    def create_linspace(self):
        self.linspace = np.linspace(0, 10, 5)

class NumpyMatrixOperations:
    def __init__(self):
        self.version = np.__version__
        self.print_version()
    
    def print_version(self):
        print("numpy version: {}".format(self.version))
    
    def add_matrices(self, matrix1, matrix2):
        return matrix1 + matrix2
    
    def subtract_matrices(self, matrix1, matrix2):
        return matrix1 - matrix2
    
    def multiply_matrices(self, matrix1, matrix2):
        return matrix1 * matrix2
    
    def divide_matrices(self, matrix1, matrix2):
        return matrix1 / matrix2
    
    def dot_product(self, matrix1, matrix2):
        return matrix1.dot(matrix2)
    
    def transpose_matrix(self, matrix):
        return matrix.T