import pandas as pd

import os

df = pd.read_excel('data/WA_Fn-UseC_-IT-Help-Desk.xlsx')

df.info()

df.to_pickle('data/data.pkl')
