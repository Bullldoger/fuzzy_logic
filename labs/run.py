from fuzzy_nums import FuzzyNumber
from fuzzy_nums.MFs import TriMF, TrapMF
from fuzzy_nums.Arithmetics import ArithmeticController

import matplotlib.pyplot as plt

f1, f2 = FuzzyNumber(sections=1000), FuzzyNumber(sections=100)
arithmetic_controller = ArithmeticController()
mf_1 = TriMF(-16, -4, -3)
mf_2 = TriMF(3, 4, 25)

f1.set_mf(mf_1)
f2.set_mf(mf_2)

f3 = f1 + f2

# f1.plot_mf()
# f2.plot_mf()
f3.plot_mf()

plt.show()