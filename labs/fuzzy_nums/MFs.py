"""

"""

import numpy as np

class Polygon:
    """

    """

    mf_type = 'Polygon'
    polygon = list()

    def __init__(self, *args):
        """

        :param args:
        """

        self.polygon = args

    def f(self, x):
        """

        :param x:
        :return:
        """
        pass

    def alpha_cut(self, alpha=1):
        """

        :param alpha:
        :return:
        """
        pass


class TriMF:
    """

    """
    a = b = c = None
    mf_type = 'TriMF'

    def __init__(self, a, b, c):
        """
        f(x|a, b, c) = max(min((x − a) / (b − a), (c − x) / (c − b)), 0)
        :return:
        :param a:
        :param b:
        :param c:
        :return:
        """
        self.a = a
        self.b = b
        self.c = c

    def f(self, x):
        """

        :param x:
        :return:
        """
        return max(min((x - self.a) / (self.b - self.a), (self.c - x) / (self.c - self.b)), 0)

    def alpha_cut(self, alpha=1):
        """

        :param alpha:
        :return:
        """
        left_values = np.linspace(self.a, self.b, 100)
        right_values = np.linspace(self.b, self.c, 100)

        left = right = 0
        for _l in left_values:
            if alpha < self.f(_l):
                left = _l
                break

        for _r in right_values:
            if alpha > self.f(_r):
                right = _r
                break

        return left, right


class TrapMF:
    """

    """
    a = b = c = d = None
    mf_type = 'TrapMF'

    def __init__(self, a, b, c, d):
        """
        f(x|a, b, c, d) = max(min( (x − a) / (b − a), 1, (d − x) / (d − c)), 0)
        :param a:
        :param b:
        :param c:
        :param d:
        :return:
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def f(self, x):
        """

        :param x:
        :return:
        """
        return  max(min((x - self.a) / (self.b - self.a), 1, (self.d - x) / (self.d - self.c)), 0)

    def alpha_cut(self, alpha=1):
        """

        :param alpha:
        :return:
        """
        left_values = np.linspace(self.a, self.b, 100)
        right_values = np.linspace(self.c, self.d, 100)

        left = right = 0
        for _l in left_values:
            if alpha < self.f(_l):
                left = _l
                break

        for _r in right_values:
            if alpha > self.f(_r):
                right = _r
                break

        if left is None:
            left = self.b
        if right is None:
            right = self.c

        return left, right


class GaussMF:
    """

    """

    mf_type = 'GaussMF'

    def __init__(self, c, sig):
        """
        f(x|c, sig) = exp{-(x - c) ** 2 / (s * sig ** 2)}
        :param c:
        :param sig:
        :return:
        """

    def f(self, x):
        """

        :param x:
        :return:
        """
    pass

    def alpha_cut(self, alpha=1):
        """

        :param alpha:
        :return:
        """
        pass