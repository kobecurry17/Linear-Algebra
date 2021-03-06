from playLa.Vector import Vector
from playLa.Matrix import Matrix
from playLa.LinearSystem import LinearSystem

if __name__ == '__main__':
    A = Matrix([[1, 2, 4], [3, 7, 2], [2, 3, 3]])
    b = Vector([7, -11, 1])
    ls = LinearSystem(A, b)
    ls.gauss_jordan_elimination()
    ls.fancy_print()
