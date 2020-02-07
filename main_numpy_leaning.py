import numpy as np

if __name__ == "__main__":
    print(np.__version__)

    lst = [1, 2, 3]
    vec = np.array(lst)
    print(vec)

    # np.array的创建
    print(np.zeros(5))
    print(np.ones(111))
    print(np.full(5, 12.4))

    # np.array的属性
    print(vec.size)
    print(len(vec))
    print(vec[-1])
    print(vec[0:2])
    print(type(vec[0:2]))

    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(2, vec2, 2 * vec2))
    print("{} * {} = {}".format(vec2, 2, vec2 * 2))
    print("{} * {} = {}".format(vec2, vec, vec2 * vec))
    print("{}.dot({}) = {}".format(vec2, vec, vec2.dot(vec)))
    #取模
    print(np.linalg.norm(vec))
    print(np.linalg.norm(vec2))
    print(vec/np.linalg.norm(vec))
    print(np.linalg.norm(vec/np.linalg.norm(vec)))