import talib
import numpy as np
import pandas as pd

# サンプルデータ作成
data = {"close": [100, 101, 102, 103, 104, 105, 104, 103, 102, 101, 100]}
df = pd.DataFrame(data)

# RSIの計算
# timeperiodがRSIを計算する時に使うデータ数
df["RSI"] = talib.RSI(df["close"], timeperiod=7)
print(df)
