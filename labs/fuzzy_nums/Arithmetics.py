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
    def compute_intervals(a, b, c, d, sign='+'):
        """

        :param a:
        :param b:
        :param c:
        :param d:
        :param sign:
        :return:
        """
        result = dict()

        result['*'] = (min(a * c, a * d, b * c, b * d), max(a * c, a * d, b * c, b * d))
        result['/'] = (min(a / c, a / d, b / c, b / d), max(a / c, a / d, b / c, b / d))

        return result[sign]

    @staticmethod
    def multiplication(a, b, c, d):
        """

        :param a:
        :param b:
        :param c:
        :param d:
        :return:
        """
        return ArithmeticController.compute_intervals(a, b, c, d, sign='*')

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
            left_1, right_1 = ArithmeticController.compute_intervals(a, b, c, d, sign='/')
        else:
            raise Exception
        return left_1, right_1
