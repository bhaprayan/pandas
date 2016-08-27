import datetime as dt
import pandas as pd
from pandas.tseries.frequencies import to_offset

d = pd.Timestamp("2000/1/1")
d + dt.timedelta(days=1)*100**25
