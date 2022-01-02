from .tensor import Tensor


def add(a, b):
    raise NotImplementedError('your code here')
    return Tensor([])


def dot(a, b):
    raise NotImplementedError('your code here')
    return Tensor([])


def mul(a, b):
    raise NotImplementedError('your code here')
    return Tensor([])


def norm(a, ord):
    raise NotImplementedError('your code here')
    return 0


def sub(a, b):
    raise NotImplementedError('your code here')
    return Tensor([])


def ones(shape):
    raise NotImplementedError('your code here')
    return Tensor([])


def randn(shape):
    from random import gauss
    return Tensor([gauss(0, 1) for _ in range(shape[0])])


def tensor(data):
    raise NotImplementedError('your code here')
    return Tensor([])


def zeros(shape):
    raise NotImplementedError('your code here')
    return Tensor([])
