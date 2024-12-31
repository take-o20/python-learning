import talib
import numpy as np
import pandas as pd

# サンプルデータ作成
data = {
    "high": [100, 101, 102, 103, 104, 105, 104, 103, 102, 101, 100],
    "low": [98, 99, 97, 101, 102, 103, 101, 100, 100, 99, 99],
}
df = pd.DataFrame(data)

# SARの計算
df["SAR"] = talib.SAR(df["high"], df["low"], acceleration=0.02, maximum=0.2)

print(df)
