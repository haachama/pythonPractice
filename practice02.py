# 載入 numpy 套件
import numpy as np

#1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
array1 = np.array(range(30))
a=np.reshape(array1,(5,6),order='F')
print(a)

#2.呈上題的array，找出被6除餘1的數的索引
b=np.where(a%6==1)
print(b)