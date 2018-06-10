import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# 将x主刻度标签设置为0.01的倍数
xmajorLocator = MultipleLocator(0.05)
# 将y轴主刻度标签设置为0.01的倍数
ymajorLocator = MultipleLocator(0.05)

plt.figure(1)
ax = plt.subplot(111)
# 在0到1之间，均匀产生100点的数组
x = np.linspace(0, 1, 100)
ax.plot(x, -x * np.log2(x))

# 设置主刻度标签的位置,标签文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

plt.show()
