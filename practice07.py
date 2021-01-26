# 載入 numpy 套件
import numpy as np

# 題目:
a = np.array([[10, 8], [3, 5]])

#1. 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
b = np.linalg.inv(a)
c = a@b
print(c)
# 是

#2. 運用上列array計算特徵值、特徵向量?
w, v = np.linalg.eig(a)
print("特徵值" ,w)
print("特徵向量" ,v)
print("========")

#3. 運用上列array計算SVD?
u, s, vh = np.linalg.svd(a)
print(u)
print(s)
print(vh)