from fuzzy_nums import FuzzyNumber
from fuzzy_nums.MFs import TriMF, TrapMF
from fuzzy_nums.Arithmetics import ArithmeticController

import matplotlib.pyplot as plt

f1, f2 = FuzzyNumber(), FuzzyNumber()
arithmetic_controller = ArithmeticController()
mf_1 = TriMF(-3, 4, 5)
mf_2 = TriMF(3, 5, 7)

f1.set_mf(mf_1)
f1.set_arithmetic_controller(arithmetic_controller)

f2.set_mf(mf_2)
f2.set_arithmetic_controller(arithmetic_controller)

f3 = f1 / f2

# f1.plot_mf()
# f2.plot_mf()
f3.plot_mf()

plt.show()