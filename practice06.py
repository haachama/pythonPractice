# 載入 numpy 套件
import numpy as np

# 題目:

#1. 將下兩列array存成npz檔
x = np.array(range(30))
y = np.array([2,3,5])

with open('multi_array.npz', 'wb') as f:
    np.savez(f, array1=x, array2=y)


#2. 讀取剛剛的npz檔，加入下列array一起存成新的npz檔

a = np.load('multi_array.npz')
z = np.random.rand(10)

with open('multi_array_new.npz', 'wb') as g:
    np.savez(g, array3=z)

