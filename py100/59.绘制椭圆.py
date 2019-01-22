import matplotlib.pyplot as plt
import numpy as np
x = y = np.arange(-10, 10, 0.1)                     #坐标系大小和精度
x, y = np.meshgrid(x,y)
plt.contour(x, y,x**2/9+y**2/3,[1])                 #椭圆函数表达式
plt.axis('scaled')
plt.show()