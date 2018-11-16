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
        return a - c, b - d

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

        if 0 <= a <= b:
            if 0 < c <= d:
                result['/'] = (a / d, b / c)
                result['*'] = (a * c, b * d)
            elif c <= 0 <= d:
                result['*'] = (b * c, b * d)
            elif c <= d < 0:
                result['/'] = (b / d, a / c)
                result['*'] = (b * c, a * d)
        elif a <= 0 <= b:
            if 0 < c <= d:
                result['/'] = (a / c, b / c)
                result['*'] = (a * c, b * d)
            elif c <= 0 <= d:
                result['*'] = (min(a * d, b * c), max(a * c, b * d))
            elif c <= d < 0:
                result['/'] = (b / d, a / d)
                result['*'] = (b * c, a * c)
        else:
            if 0 < c <= d:
                result['/'] = (a / c, b / d)
                result['*'] = (a * d, b * c)
            elif c <= 0 < d:
                result['*'] = (a * d, a * c)
            elif c <= d < 0:
                result['/'] = (b / c, b / d)
                result['*'] = (b * d, a * c)

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
    def division(a, b, c, d, abs_const=1e-1):
        """

        :param abs_const:
        :param a:
        :param b:
        :param c:
        :param d:
        :return:
        """

        if c == 0 or d == 0:
            if c == 0 and d > 0:
                left_1, right_1 = ArithmeticController.compute_intervals(a, b, 0 + abs_const, d, sign='/')
            elif c < 0 and d == 0:
                left_1, right_1 = ArithmeticController.compute_intervals(a, b, c, 0 + abs_const, sign='/')
            else:
                left_1, right_1 = ArithmeticController.compute_intervals(a, b, abs_const, abs_const, sign='/')
        if c <= 0 <= d:
            _c = 0 - abs_const
            _d = 0 + abs_const

            left_1, right_1 = ArithmeticController.compute_intervals(a, b, c, _c, sign='/')
            left_2, right_2 = ArithmeticController.compute_intervals(a, b, _d, d, sign='/')

            left_1 = min(left_1, left_2)
            right_1 = max(right_1, right_2)
        elif c * d > 0:
            left_1, right_1 = ArithmeticController.compute_intervals(a, b, c, d, sign='/')

        return left_1, right_1
