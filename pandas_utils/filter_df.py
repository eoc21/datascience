__author__ = 'Ed Cannon'

import pandas as pd
import sys

def load_csv(file_name):
    df = pd.read_csv(file_name)
    return df

def filter_numeric_col_by_range(df,col,start,end):
    '''
    :param df: input dataframe to filter
    :param col: string title of column to filter
    :param start: min value to include in filter
    :param end: max value to include in fitler
    :return: filtered data frame
    '''
    df2 = df[(df[col] > start) & (df[col] < end)]
    return df2

if __name__ == '__main__':
    df = load_csv(sys.argv[1])
    df2 = filter_numeric_col_by_range(df,'sepal length',5.7,6.0)