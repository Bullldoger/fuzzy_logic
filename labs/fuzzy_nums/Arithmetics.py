"""

"""


class ArithmeticController:
    """

    """

    def __init__(self):
        pass

    @staticmethod
    def addition(a, b, c, d):
        """

        :param a:
        :param b:
        :param c:
        :param d:
        :return:
        """
        return a + c, b + d

    @staticmethod
    def subtraction(a, b, c, d):
        """

        :param a:
        :param b:
        :param c:
        :param d:
        :return:
        """
        return a - d, b - c

    @staticmethod
    def multiplication(a, b, c, d):
        """

        :param a:
        :param b:
        :param c:
        :param d:
        :return:
        """

        left, right = (min(a * c, a * d, b * c, b * d), max(a * c, a * d, b * c, b * d))

        return left, right

    @staticmethod
    def division(a, b, c, d):
        """

        :param abs_const:
        :param a:
        :param b:
        :param c:
        :param d:
        :return:
        """

        if c * d > 0:
            left, right = (min(a / c, a / d, b / c, b / d), max(a / c, a / d, b / c, b / d))
        else:
            raise Exception

        return left, right
