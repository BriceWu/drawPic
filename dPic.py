import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# 将x主刻度标签设置为0.01的倍数
x_major_Locator = MultipleLocator(0.05)
# 将y轴主刻度标签设置为0.01的倍数
y_major_Locator = MultipleLocator(0.05)

plt.figure(1)
plt.grid(True, linestyle="-", color="b", linewidth="0.5")
ax = plt.subplot(111)
# 在0到1之间，均匀产生100点的数组
x = np.linspace(0, 1, 100)
ax.plot()
ax.plot(x, -x * np.log2(x))

# 设置主刻度标签的位置,标签文本的格式
ax.xaxis.set_major_locator(x_major_Locator)
ax.yaxis.set_major_locator(y_major_Locator)

plt.show()
