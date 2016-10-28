import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,2,5,np.nan, 6, 8])
print s
dates = pd.date_range('20130101', periods = 6)
df = pd.DataFrame(np.random.randint(1,10,[6,4]), index = dates, columns = list('ABCD'))
print df
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('02/10/2013').dayofweek,
                    'C' : pd.Series(1, index=range(4), dtype = 'float32'),
                    'D' : np.array([3]*4, dtype = 'int32'),
                    'E' : pd.Categorical(["test", "train", "test", "train"]),
                    'F' : 'foo'})
print df2
print df2.tail(2)
print df.index
print df2.columns
print df2.values
print df.describe()
print df.T
print df.sort_index(axis = 0, ascending = False)
print df.sort_index(axis = 0, ascending = False)
print df.sort_index(axis = 0)
print df.sort_values(by='B')
print '---'
print df.sort_values(by='B',ascending = False)['B'].unique()
print df.sort_values(by='B',ascending = False)['B'].unique()[:2] #find the 2nd largest
print df.sort_values(by='B',ascending = False)['B'].unique()[1] #find the 2nd largest

#Selection
print df['A']
print df[0:3]
print df['20130101':'20130103']

#Selection by Label
print df.loc[dates[0]]
print df.loc[:, ['A','B']]
print df.loc['20130101':'20130103', ['A','B']]
print df.loc['20130103', ['A','B']]

#For getting a scalar value
print df.loc['20130101','A']
print df.loc[dates[0],'A']

#Selection by Position
print df.iloc[3]
print df.iloc[3:5,0:2]
print df.iloc[[3,5], [0,3]]
print df.iloc[1:3,:]
print df.iat[1,1]

#Boolean Indexing
print df[df.A > 3]  # Using a single column values to select data.
print df[df>3] # A where operation for getting.

#Using the isin() method for filtering:
df2 = df.copy()
df2['E'] = ['one','two','two','three','one','four']
# print df2[df2.E.isin(['two','four'])]
print df2[df2['E'].isin(['two','four'])]

#Setting
s1 = pd.Series(range(6),index = pd.date_range('20130101',periods = 6))
print s1
df['F'] = s1
df.at[dates[0],'A'] = 0
df.iat[0,1] = 0
df.iloc[0,2] = 0
# df.iat[[3,5], [0,3]] = 0 #not ok, must use interger to index
f = lambda x: x*5
# df.loc[:,'D'] = np.array([5]*len(df))
print df['D'].map(lambda x: x*5) #must save back, otherwise will not save results
# df.columns = [x.lower() for x in df.columns] #operation on columns
df1 = df.applymap(lambda x: float(x) *2)
# dates = range(6)
# df = pd.DataFrame(np.random.randint(1,10,[6,4]), index = dates, columns = list('ABCD'))
df2 = df1.copy()
df3 = df1.copy()
df3.iloc[0,0] = 100
df3.iloc[0,3] = 100
df2[df2>0] = -df3
print df3
print df2[df2<0]
print "-------"
B = np.arange(6)
print df2.shape, B.shape #shape is tuple
print df2
print df2[['B','C']].apply(lambda x: x*B) #column to column multiplication
print (df2.T*B).T
C = np.arange(5)
print df2*C
print df

# Missing data
df1 = df.reindex(index = dates[0:4], columns = list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
df1.loc[dates[0], 'F'] = np.nan
print df1.dropna(how='all')
print df1.fillna(value = 5)
print df1.fillna(5)
print df1.isnull()
print df1.isnull().sum()

#Operations -stats
print df1.mean(1) #horizontal
print df1.mean() #vertical
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)

