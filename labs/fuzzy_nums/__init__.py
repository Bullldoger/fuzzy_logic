"""

"""
import fuzzy_nums
from fuzzy_nums.MFs import GaussMF, Polygon, TrapMF, TriMF
from fuzzy_nums.Arithmetics import ArithmeticController

import numpy as np


class FuzzyNumber:
    """

    """
    mf_func = None
    arithmetic_controller = None
    sections = 10

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

    def get_alpha_cut(self, alpha=1):
        """

        :param alpha:
        :return:
        """
        return self.mf_func.alpha_cut(alpha=alpha)

    def handle_operation(self, other, operation='+'):
        """

        :param other:
        :param operation:
        :return:
        """

        left, right = list(), list()
        result = list()

        for alpha in np.linspace(0, 1, self.sections):
            a_1, b_1 = self.get_alpha_cut(alpha=alpha)
            a_2, b_2 = other.get_alpha_cut(alpha=alpha)

            a, b = 0, 0

            if operation == '+':
                a, b = self.arithmetic_controller.addition(a_1, b_1, a_2, b_2)
            elif operation == '-':
                a, b = self.arithmetic_controller.subtraction(a_1, b_1, a_2, b_2)
            elif operation == '*':
                a, b = self.arithmetic_controller.multiplication(a_1, b_1, a_2, b_2)
            elif operation == '/':
                a, b = self.arithmetic_controller.division(a_1, b_1, a_2, b_2)

            left.append((a, alpha))
            right.append((b, alpha))

        result = left + [i for i in reversed(right)]

        result_number = FuzzyNumber()
        arithmetic_controller = ArithmeticController()
        mf_function = Polygon(result)

        result_number.set_arithmetic_controller(arithmetic_controller)
        result_number.set_mf(mf_function)

        return result_number

    def __add__(self, other):
        """

        :param fuzzy_num:
        :return:
        """
        return self.handle_operation(other, operation='+')

    def __sub__(self, other):
        """

        :param other:
        :return:
        """
        return self.handle_operation(other, operation='-')

    def __mul__(self, other):
        """

        :param other:
        :return:
        """
        return self.handle_operation(other, operation='*')

    def __truediv__(self, other):
        """

        :param other:
        :return:
        """
        return self.handle_operation(other, operation='/')
