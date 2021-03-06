# 載入 numpy 套件
import numpy as np

#1.
# 正常的談話的聲壓為20000微巴斯卡，請問多少分貝?
#請寫下程式

V1 = 20000
V0 = 20

a = 20*np.log10(V1/V0)
print(a)

#2.
# 30分貝的聲壓會是50分貝的幾倍?
# 公式移項過後可以得到 V1 = ?
#請寫下程式

def Pascal(db):
    return 20*np.power(10, db/20)
b = Pascal(30)/Pascal(50)
print(b)

