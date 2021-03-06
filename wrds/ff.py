import pandas as pd
from pandas.io.data import DataReader
import datetime as dt

def factors_df(end=True):
    ff = pd.DataFrame(DataReader("F-F_Research_Data_Factors", "famafrench")[0])
    ff.columns = ['Mkt_rf', 'SMB', 'HML', 'rf']

    ff.index = [dt.datetime(d/100, d%100, 1) for d in ff.index]
    if end:
        ff.index = ff.index.to_period('M').to_timestamp('M')

    return ff
