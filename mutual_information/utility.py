#%% Load the Cryptocurrency data
import os 
import pandas as pd

# Load Data
def load_currency(name,columns):
    path = "../Data/dataset"
    df = pd.read_csv(os.path.join(path,name+'_merged.txt'), sep = ',', header=0)
    df.time = pd.to_datetime(df.time,unit='s')
    df = df.set_index('time')
    df = df[columns]
    return df

# # Example
# columns = ['close','logclose']
# df = load_currency(name = "BTC",columns=columns)

#%%

def load_all_currencies(names,columns):
    path = "../Data/dataset"

    li = []

    for curr in names:
        df = pd.read_csv(os.path.join(path,curr+'_merged.txt'), sep = ',', header=0)
        df.time = pd.to_datetime(df.time,unit='s')
        df = df.set_index('time')
        df = df[columns]
        li.append(df)    


    frame = pd.concat(li,axis=1,keys=names,join='outer')

    # Pick common time window of all currencies
    frame = frame.dropna(axis=0)
    return frame

# # Example
# names = ["DASH", "ETC", 'ETH']
# columns = ['close','logclose']

# df = load_all_currencies(names,columns)