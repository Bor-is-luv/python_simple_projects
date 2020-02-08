import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

x = np.linspace(-10, 10, 1000)
y = 1+np.sinc(x)

ax = plt.subplot(111)
ax.plot(x, y, lw=2)
ax.fill_between(x, 0, y, alpha=0.2)
ax.grid()

majorLocator = MultipleLocator(1)
ax.xaxis.set_major_locator(majorLocator)

plt.show()
