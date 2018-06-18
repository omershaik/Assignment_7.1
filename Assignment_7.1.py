# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:36:29 2018

@author: Zakir
"""

import numpy as np
import pandas as pd

#Given dataframe
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

# 1. Fill in these missing numbers and make the column an integer column
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)

# 2. Split each string on the underscore delimiter _ to give a new temporary DataFrame with the correct values.
df1 = df['From_To'].str.split('_',expand=True)
df1.rename(columns={0: 'From', 1: 'To'}, inplace=True)

#3. Standardise the strings so that only the first letter is uppercase
df1 = df1.apply(lambda x: x.astype(str).str.capitalize())


#4. attach the temporary DataFrame from the previous questions.
df = df.drop('From_To', axis=1)
newDf = pd.concat([df, df1], axis=1)

#5. each first value in its own column, each second value in its owncolumn, and so on.
delays = df['RecentDelays'].apply(pd.Series)

#6. renmaing delays column and concatinating it to the original dataframe
delays.rename(columns={0: 'delay_1', 1: 'delay_2', 2: 'delay_3'}, inplace=True)
newDf = pd.concat([newDf, delays], axis =1)
newDf = newDf.drop('RecentDelays', axis =1)