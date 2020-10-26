# fufu F87441C
# fufu 2020/9/16 14:12

#my_df['DCS_Y_or_N'][my_df[field].str.contains('|'.join(values), case=False)] = 'N'

import pandas as pd
SS = ['og','H,PM']

dfh = pd.read_csv('D:/users/f87441c/Desktop/fufu111.csv', encoding="utf-8")  #unicode_escape
print(dfh)

#s1 = pd.Series(['Mouse', 'dog', 'house and parrot','23,EE'])
print(dfh['PO Item Short Text'].str.contains('|'.join(SS)))

