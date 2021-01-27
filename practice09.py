# 載入 numpy 套件
import pandas as pd

# 題目:
# 讀取資料夾中boston.csv讀取其欄位CHAS、NOX、RM，輸出成.xlsx檔案

a = pd.read_csv('boston.csv',usecols=['CHAS','NOX','RM'])
print(a)
a.to_excel('a.xlsx',sheet_name='boston')