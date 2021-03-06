"""

"""

import fuzzy_nums
from fuzzy_nums.MFs import GaussMF, Polygon, TrapMF, TriMF
from fuzzy_nums.Arithmetics import ArithmeticController

import numpy as np
from matplotlib import pyplot as plt


class FuzzyNumber:
    """

    """

    mf_func = None
    arithmetic_controller = None
    sections = None
    left = right = None

    def __init__(self, sections=10):
        """

        """
        self.sections = sections
        self.arithmetic_controller = ArithmeticController()

    def set_mf(self, mf_func):
        """

        :param mf_func:
        :return:
        """
        self.mf_func = mf_func
        self.left = self.mf_func.left_value
        self.right = self.mf_func.right_value

    def set_arithmetic_controller(self, arithmetic_controller):
        """

        :param arithmetic_controller:
        :return:
        """
        self.arithmetic_controller = arithmetic_controller

    def get_alpha_cut(self, alpha=1, sections=10):
        """

        :param alpha:
        :return:
        """
        return self.mf_func.alpha_cut(alpha=alpha, sections=sections)

    def handle_operation(self, other, operation='+'):
        """

        :param other:
        :param operation:
        :return:
        """

        left, right = list(), list()

        for alpha in np.linspace(0, 1, max(self.sections, other.sections)):
            a_1, b_1 = self.get_alpha_cut(alpha=alpha, sections=self.sections)
            a_2, b_2 = other.get_alpha_cut(alpha=alpha, sections=self.sections)

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

        result = left + [i for i in right]
        result = sorted(result, key=lambda x: x[0])

        result_number = FuzzyNumber(sections=max(self.sections, other.sections))
        mf_function = Polygon(result)

        result_number.set_mf(mf_function)

        return result_number

    def __add__(self, other):
        """

        :param other:
        :return:
        """

        if type(other) is int or type(other) is float:
            other = self.crisp_to_fuzzy(other)

        return self.handle_operation(other, operation='+')

    def __sub__(self, other):
        """

        :param other:
        :return:
        """

        if type(other) is int or type(other) is float:
            other = self.crisp_to_fuzzy(other)

        return self.handle_operation(other, operation='-')

    def __mul__(self, other):
        """

        :param other:
        :return:
        """

        if type(other) is int or type(other) is float:
            other = self.crisp_to_fuzzy(other)

        return self.handle_operation(other, operation='*')

    def __truediv__(self, other):
        """

        :param other:
        :return:
        """

        if type(other) is int or type(other) is float:
            other = self.crisp_to_fuzzy(other)

        return self.handle_operation(other, operation='/')

    @staticmethod
    def crisp_to_fuzzy(crisp):
        """

        :param crisp:
        :return:
        """
        _other = FuzzyNumber()
        mf_func = TriMF(crisp - 1e-10, crisp, crisp + 1e-10)
        arithmetic_controller = ArithmeticController()
        _other.set_arithmetic_controller(arithmetic_controller)
        _other.set_mf(mf_func)
        return _other

    def plot_mf(self, size=(8, 5)):
        """

        :return:
        """

        if self.mf_func.mf_type == 'polygon':
            values = [ v for v, _ in self.mf_func.polygon ]
            affiliation = [alpha for _, alpha in self.mf_func.polygon]
        else:
            values = np.linspace(self.left, self.right, self.sections)
            affiliation = np.array([self.mf_func.f(v) for v in values])

        plt.figure(figsize=size)
        plt.plot(values, affiliation, 'b', label='Membership function')
        plt.title('Fuzzy Number', fontsize=20)
        plt.ylabel('Affiliation', fontsize=16)
        plt.xlabel('Value', fontsize=16)
        plt.legend()
        plt.grid()
