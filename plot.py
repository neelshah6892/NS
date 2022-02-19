import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],colu
   mns = ['col2','col1'])

sorted_df=unsorted_df.sort_index()
print(sorted_df)


def report_diff(x):
    return x[0] if x[0] == x[1] else '{} ---> {}'.format(*x)