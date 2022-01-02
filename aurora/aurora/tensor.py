class Tensor:
    def __init__(self, data):
        import array
        for x in data:
            if isinstance(x, int) or isinstance(x, float):
                continue
            raise TypeError('now we should support only 1d tensors')

        self.__data = array.array('f', data)
        self.__shape = (len(data), )

    @property
    def shape(self):
        return self.__shape

    def __repr__(self):
        return f"Tensor([{', '.join([f'{x:.4f}' for x in self.__data])}])"

    def isclose(self, other):
        from math import isclose
        return all([isclose(a, b, abs_tol=1e-5) for a, b in zip(self.__data, other.__data)])

    def add(self, other):
        raise NotImplementedError('your code here')
        return Tensor([])

    def dot(self, other):
        raise NotImplementedError('your code here')
        return 0

    def mul(self, scalar):
        raise NotImplementedError('your code here')
        return Tensor([])

    def norm(self, ord=2):
        if ord != 1 and ord != 2:
            raise ValueError('illegal ord value')

        raise NotImplementedError('your code here')
        return 0

    def sub(self, other):
        raise NotImplementedError('your code here')
        return Tensor([])

    def __add__(self, other):
        raise NotImplementedError('your code here')
        return Tensor([])

    def __mul__(self, other):
        raise NotImplementedError('your code here')
        return Tensor([])

    def __neg__(self):
        raise NotImplementedError('your code here')
        return Tensor([])

    def __rmul__(self, other):
        raise NotImplementedError('your code here')
        return Tensor([])

    def __sub__(self, other):
        raise NotImplementedError('your code here')
        return Tensor([])

    def __matmul__(self, other):
        raise NotImplementedError('your code here')
        return 0

    def __eq__(self, other):
        return self.isclose(other)
