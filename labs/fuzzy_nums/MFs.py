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