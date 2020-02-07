from playLa.Matrix import Matrix
from playLa.Vector import Vector
import numpy as np

if __name__ == "__main__":
    matrix = Matrix([[1, 2], [3, 4]])
    # print(matrix)
    # print(matrix.shape())
    # print(matrix.row_num())
    # print(len(matrix))
    # print(matrix.col_vector(1))
    other = Matrix([[6, 7], [8, 9], [10, 11]])
    # print("add:{}".format(matrix + other))
    # print("subtract:{}".format(other - matrix))
    # print("scalar-mul:{}".format(matrix * 2))
    # print("scalar-mul:{}".format(2 * matrix))
    # print("zero_2_3: {}".format(Matrix.zero(2, 3)))

    # T = Matrix([[1.5, 0], [0, 2]])
    # p = Vector([5, 3])
    # print("T.dot(p) = {}".format(T.dot(p)))
    #
    # P = Matrix([[0, 4, 5], [0, 0, 3]])
    # print("T.dot(P) = {}".format(T.dot(P)))
    # print("P.T() = {}".format(P.T()))
    # print(matrix)
    # print(matrix.dot(Matrix.identity(2)))
    A = np.array([[1, 2], [3, 4]])
    invA = np.linalg.inv(A)
    # print(invA)
    print(invA)
    print(np.linalg.inv(A.T()))
