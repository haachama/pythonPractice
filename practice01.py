# 載入 numpy 套件
import numpy as np

data=np.arange(0,21,1)  # 第一題 生成一個等差數列，首數為0，尾數為20，公差為1的數列。
print(data)

print(data[::2])  # 第二題 呈上題，將以上數列取出偶數。

print(data[::3])  #3.呈1題，將數列取出3的倍數。