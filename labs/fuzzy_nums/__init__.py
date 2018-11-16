"""

"""


class Polygon:
    """

    """

    mf_type = 'Polygon'

    def __init__(self, *args, **kwargs):
        pass

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


class TrapMF:
    """

    """

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


class ArithmeticController:
    """

    """

    def __init__(self):
        pass

    @staticmethod
    def addition(a_1, b_1, a_2, b_2):
        """

        :param a_1:
        :param b_1:
        :param a_2:
        :param b_2:
        :return:
        """
        pass

    @staticmethod
    def subtraction(a_1, b_1, a_2, b_2):
        """

        :param a_1:
        :param b_1:
        :param a_2:
        :param b_2:
        :return:
        """
        pass

    @staticmethod
    def multiplication(a_1, b_1, a_2, b_2):
        """

        :param a_1:
        :param b_1:
        :param a_2:
        :param b_2:
        :return:
        """
        pass

    @staticmethod
    def division(a_1, b_1, a_2, b_2):
        """

        :param a_1:
        :param b_1:
        :param a_2:
        :param b_2:
        :return:
        """
        pass


class FuzzyNumber:
    """

    """
    mf_func = None
    arithmetic_controller = None

    def __init__(self):
        pass

    def set_mf(self, mf_func):
        """

        :param mf_func:
        :return:
        """
        self.mf_func = mf_func

    def set_arithmetic_controller(self, arithmetic_controller):
        """

        :param arithmetic_controller:
        :return:
        """
        self.arithmetic_controller = arithmetic_controller

    def __add__(self, other):
        """

        :param fuzzy_num:
        :return:
        """
        pass

    def __sub__(self, other):
        """

        :param other:
        :return:
        """
        pass

    def __mul__(self, other):
        """

        :param other:
        :return:
        """
        pass

    def __truediv__(self, other):
        """

        :param other:
        :return:
        """
        pass
