import matplotlib.pyplot as plt
import numpy as np

f = lambda x: x**3 + 0.2*x**5 + x
x = np.linspace(-2, 2, 400)
y = f(x)

f1 = 3*x*2 + x**4 + 1
f2 = 6*x + 4*x**3

poi_x_candidates = np.roots([4, 0, 6, 0])