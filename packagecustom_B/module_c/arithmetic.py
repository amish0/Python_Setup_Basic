# python basic arithmetic operation
#
import numpy as np
import sys

class ArithmeticOps:
    def __init__(self) -> None:
        self.version = np.__version__
        self.print_version()
    
    def print_version(self):
        print("numpy version: {}".format(self.version))
    
    def add(self, a, b):
        return np.add(a, b)
    
    def subtract(self, a, b):
        return np.subtract(a, b)
    
    def multiply(self, a, b):
        return np.multiply(a, b)
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return np.divide(a, b)
    
    def power(self, a, b):
        return np.power(a, b)
    
    def square_root(self, a):
        return np.sqrt(a)
    
    def absolute(self, a):
        return np.abs(a)
    
    def exponential(self, a):
        return np.exp(a)

class PythonArithmeticsOps:
    def __init__(self) -> None:

        # python version
        self.version = (sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
        self.print_version()
    
    def print_version(self):
        print("python version: {}.{}.{}".format(self.version[0], self.version[1], self.version[2]))
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        return a ** b
    
    def square_root(self, a):
        return a ** 0.5
    
    def absolute(self, a):
        return abs(a)
    
    def exponential(self, a):
        return np.exp(a)
    
if __name__ == "__main__":
    # Example usage:
    a = 10
    b = 20
    print("a = {}, b = {}".format(a, b))
    print("Addition: {}".format(ArithmeticOps().add(a, b)))
    print("Subtraction: {}".format(ArithmeticOps().subtract(a, b)))
    print("Multiplication: {}".format(ArithmeticOps().multiply(a, b)))
    print("Division: {}".format(ArithmeticOps().divide(a, b)))
    print("Power: {}".format(ArithmeticOps().power(a, b)))
    print("Square Root: {}".format(ArithmeticOps().square_root(a)))
    print("Absolute: {}".format(ArithmeticOps().absolute(a)))
    print("Exponential: {}".format(ArithmeticOps().exponential(a)))
    print("Python Addition: {}".format(PythonArithmeticsOps().add(a, b)))
    print("Python Subtraction: {}".format(PythonArithmeticsOps().subtract(a, b)))
    print("Python Multiplication: {}".format(PythonArithmeticsOps().multiply(a, b)))
    print("Python Division: {}".format(PythonArithmeticsOps().divide(a, b)))
    print("Python Power: {}".format(PythonArithmeticsOps().power(a, b)))
    print("Python Square Root: {}".format(PythonArithmeticsOps().square_root(a)))
    print("Python Absolute: {}".format(PythonArithmeticsOps().absolute(a)))
    print("Python Exponential: {}".format(PythonArithmeticsOps().exponential(a)))