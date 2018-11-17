from fuzzy_nums import FuzzyNumber
from fuzzy_nums.MFs import TriMF, TrapMF
from fuzzy_nums.Arithmetics import ArithmeticController

import matplotlib.pyplot as plt

sections = 3

f1, f2 = FuzzyNumber(sections=sections), FuzzyNumber(sections=sections)
arithmetic_controller = ArithmeticController()
mf_1 = TriMF(-3, 4, 5)
mf_2 = TriMF(3, 5, 7)

f1.set_mf(mf_1)
f2.set_mf(mf_2)

f3 = f1 * f2

# f1.plot_mf()
# f2.plot_mf()
f3.plot_mf()

plt.show()