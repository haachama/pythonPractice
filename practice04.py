# 載入 numpy 套件
import numpy as np

# 題目:
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])
# 上3列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，舉例第一位同學英文55分、數學60分、國文65分，運用上列數據回答下列問題。

#1.有多少學生英文成績比數學成績高?

a = np.greater(english_score , math_score)
a = np.where(a==True)
a = np.size(a)
print(a)

#2.是否全班同學最高分都是國文?
b = np.greater(chinese_score,math_score)
print(b)
c = np.greater(chinese_score,english_score)
print(c)

print(np.logical_and(b,c))
print(np.logical_and(b,c).all())
