"""

"""

import numpy as np


class Polygon:
    """

    """
    left_value = right_value = None
    mf_type = 'polygon'
    polygon = list()

    x = []
    y = []
    
    def __init__(self, *args):
        """

        :param args:
        """

        self.polygon = args[0]
        self.left_value = self.polygon[0][0]
        self.right_value = self.polygon[-1][0]

    def f(self, x):
        """

        :param x:
        :return:
        """
        for (point_l, alpha_l), (point_r, alpha_r) in zip(self.polygon[:-1], self.polygon[1:]):
            if point_l <= x < point_r:
                return alpha_l

        return 0

    def alpha_cut(self, alpha=1, sections=10):
        """

        :param sections:
        :param alpha:
        :return:
        """
        left_values = np.linspace(self.left_value, self.right_value, sections)
        right_values = reversed(np.linspace(self.left_value, self.right_value, sections))

        left = right = 0
        for _l in left_values:
            if alpha <= self.f(_l):
                left = _l
                break

        for _r in right_values:
            if alpha >= self.f(_r):
                right = _r
                break

        return left, right


class TriMF:
    """

    """
    left_value = right_value = None
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

        self.left_value = a
        self.right_value = c

    def f(self, x):
        """

        :param x:
        :return:
        """
        return max(min((x - self.a) / (self.b - self.a), (self.c - x) / (self.c - self.b)), 0)

    def alpha_cut(self, alpha=1, sections=10):
        """

        :param sections:
        :param alpha:
        :return:
        """
        left_values = np.linspace(self.a, self.b, sections)
        right_values = np.linspace(self.b, self.c, sections)

        left = right = 0
        for _l in left_values:
            if alpha <= self.f(_l):
                left = _l
                break

        for _r in right_values:
            if alpha >= self.f(_r):
                right = _r
                break

        return left, right


class TrapMF:
    """

    """
    left_value = right_value = None
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

        self.left_value = a
        self.right_value = d

    def f(self, x):
        """

        :param x:
        :return:
        """
        return  max(min((x - self.a) / (self.b - self.a), 1, (self.d - x) / (self.d - self.c)), 0)

    def alpha_cut(self, alpha=1, sections=10):
        """

        :param sections:
        :param alpha:
        :return:
        """
        left_values = np.linspace(self.a, self.b, sections)
        right_values = np.linspace(self.c, self.d, sections)

        left = right = 0
        for _l in left_values:
            if alpha <= self.f(_l):
                left = _l
                break

        for _r in right_values:
            if alpha >= self.f(_r):
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
