import pandas as pd

# 題目:

#讀取STOCK_DAY_0050_202009.csv、STOCK_DAY_0050_202010.csv
a = pd.read_csv('STOCK_DAY_0050_202009.csv')
b = pd.read_csv('STOCK_DAY_0050_202010.csv')
# print(a)
# print(b)

#串聯
c = pd.concat([a,b],axis=0,join='inner')
print(c)

#找出open小於close的資料
d = c.loc[c.open<c.close,['open','close']]
print(d) 