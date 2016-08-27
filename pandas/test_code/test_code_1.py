import pandas as pd
from pandas.tseries.frequencies import to_offset

d = pd.Timestamp("2000/1/1")
d + to_offset("D")*100**25
