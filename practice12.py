import pandas as pd
import numpy as np
import matplotlib as plt

# 題目: 
# 將資料夾中boston.csv讀進來，並用圖表分析欄位。
# 1.畫出箱型圖，並判斷哪個欄位的中位數在300~400之間?
# 欄位TAX
df = pd.read_csv("boston.csv")
df.boxplot()
# 2.畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係?
#成反比關係
df.plot.scatter(x='RM', y='LSTAT')
