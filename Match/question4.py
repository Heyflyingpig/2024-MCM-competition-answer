import numpy as np
import matplotlib.pyplot as plt

# 定义已知参数
Z_alpha = 1.96  # 例如，95%置信水平的Z值
Z_beta = 1.28   # 例如，80%置信水平的Z值

# 设置随机抽样的次数
num_samples = 8

# 定义离散的n值和p0值
N = np.random.uniform(700, 900, num_samples)
k = np.random.uniform(76, 88, num_samples)
p0_values = k/N

# 创建网格
k, P0 = np.meshgrid(N, p0_values)

# 计算p1
P1 = (Z_alpha / 2) ** 2 * P0 * (1 - P0) + Z_beta ** 2 * (N * (P0 - 1) + P0 ** 2) / (N - P0)

# 计算p1的均值
mean_P1 = np.mean(P1, axis=0)  # 按行对p1求均值

# 为柱状图准备数据
x_vals = N.flatten()
y_vals = k.flatten()
z_vals = np.zeros_like(x_vals)  # z轴从0开始

# 绸树柱子的宽度
dx = 3  # 柱子的宽度
dy = 0.03  # 柱子的深度
dz = P1.flatten()

# 绘制三维柱状图
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制柱子
ax.bar3d(x_vals, y_vals, z_vals, dx, dy, dz, color='cyan', alpha=0.7)

# 设置标题和标签
ax.set_title('3D Bar Plot of p1 = f(n, p0)')
ax.set_xlabel('N axis (Sample Size)')
ax.set_ylabel('P0 axis')
ax.set_zlabel('P1 axis')

plt.show()