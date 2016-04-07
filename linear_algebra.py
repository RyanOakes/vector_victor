class ShapeError(Exception):
    pass


def shape(vector):
    return (len(vector),)


# m = [3, 4]
# n = [5, 0]
#
# v = [1, 3, 0]
# w = [0, 2, 4]
# u = [1, 1, 1]
# y = [10, 20, 30]
# z = [0, 0, 0]


def vector_add(vec_1, vec_2):
    if len(vec_1) != len(vec_2):
        raise ShapeError()

    return [x + y for x, y in zip(vec_1, vec_2)]


def vector_sub(vec_1, vec_2):
    if len(vec_1) != len(vec_2):
        raise ShapeError()

    return [x - y for x, y in zip(vec_1, vec_2)]


def vector_sum(*args):

    lengths = [len(x) for x in args]
    return [x == y for x, y in lengths]

    #different way to solve above issue
    # length = [len(i) for i args]
    # if max(length) != min(length):
    #     raise ShapeError

    # return [sum(a) for a in zip(*args)]


def dot(vec_1, vec_2):
    return sum([vec_1[i] * vec_2[i] for i in range(len(vec_1))])
    #return sum([a * b for a, b in zip(vector1, vector2)])

def vector_mean(*args):
    return[x/len(args) for x in vector_sum(*args)]
