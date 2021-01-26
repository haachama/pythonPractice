# 載入 numpy 套件
import numpy as np

# 題目:
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])

# 上3列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，舉例第一位同學英文55分、數學60分、國文65分，今天第五位同學因某原因沒來考試，導致數學成績缺值，運用上列數據回答下列問題。

#1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
enMean =  np.array(english_score)
if not np.isnan(np.sum(enMean)):
    print("陣列中無 nan，忽略 nan 後的平均值為：", np.mean(enMean))
else:
    print("陣列中有 nan，忽略 nan 後的平均值為：", np.nanmean(enMean))

maMean = np.array(math_score)
if not np.isnan(np.sum(maMean)):
    print("陣列中無 nan，忽略 nan 後的平均值為：", np.mean(maMean))
else:
    print("陣列中有 nan，忽略 nan 後的平均值為：", np.nanmean(maMean))

chMean = np.array(chinese_score)
if not np.isnan(np.sum(chMean)):
    print("陣列中無 nan，忽略 nan 後的平均值為：", np.mean(chMean))
else:
    print("陣列中有 nan，忽略 nan 後的平均值為：", np.nanmean(chMean))
print("=========")
a = np.max(english_score)
b = np.nanmax(math_score)
c = np.max(chinese_score)
d = np.min(english_score)
e = np.nanmin(math_score)
f = np.min(chinese_score)
g = np.std(english_score)
h = np.nanstd(math_score)
i = np.std(chinese_score)
print("英文成績最大值為" ,a, "最小值為" ,d, "標準差為" ,g)
print("數學成績最大值為" ,b, "最小值為" ,e, "標準差為" ,h)
print("國文成績最大值為" ,c, "最小值為" ,f, "標準差為" ,i)
print("=========")

#2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
math_score[4] = 55
maMeanNew = np.array(math_score)
if not np.isnan(np.sum(maMeanNew)):
    print("陣列中無 nan，忽略 nan 後的平均值為：", np.mean(maMeanNew))
else:
    print("陣列中有 nan，忽略 nan 後的平均值為：", np.nanmean(maMeanNew))
j = np.max(maMeanNew)
k = np.min(maMeanNew)
l = np.std(maMeanNew)
print("補考後數學成績最大值為" ,j, "最小值為" ,k, "標準差為" ,l)
print("=========")

#3. 用補考後資料找出與國文成績相關係數最高的學科?
y = np.corrcoef(chinese_score,english_score)
print(y)
z = np.corrcoef(chinese_score,maMeanNew)
print(z)
