__author__ = 'Ed Cannon'
#groupby multiple columns: grouped = df.groupby(['A', 'B'])
import pandas as pd
from filter_df import load_csv
import sys

def groupby_single_column(df,col,oper):
    '''
    aggregation functions available: mean, sum, size, count, std, var, sem, describe, first, last, nth, min, max

    :param df: input data frame
    :param col: column to group by
    :param oper: operation to apply to groupby
    :return: groupy data frame
    '''
    if oper == 'sum':
        return df.groupby(col).sum()
    elif oper == 'mean':
        return df.groupby(col).mean()
    elif oper == 'std':
        return df.groupby(col).std()
    elif oper == 'count':
        return df.groupby(col).count()
    elif oper == 'describe':
        return df.groupby(col).describe()
    else:
        return df

if __name__ == '__main__':
    df = load_csv(sys.argv[1])
    print groupby_single_column(df,'class','mean')
