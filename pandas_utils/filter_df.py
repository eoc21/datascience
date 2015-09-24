__author__ = 'Ed Cannon'

import pandas as pd
import sys

def load_csv(file_name):
    df = pd.read_csv(file_name)
    return df

def filter_numeric_col_by_range(df,col,start,end):
    '''
    :param df: input data frame to filter
    :param col: string title of column to filter
    :param start: min value to include in filter
    :param end: max value to include in fitler
    :return: filtered data frame
    '''
    df2 = df[(df[col] > start) & (df[col] < end)]
    return df2

def filter_by_string(df,col,filter_str):
    '''
    :param df: input data frame
    :param col: column to filter by string
    :param filter_str: filter query
    :return: filtered data frame
    '''
    return df[df[col].str.contains(filter_str)]

def filter_exact_match(df,col,match_val):
    '''
    Filter a column for exact match
    either string or numeric.
    :param df:
    :param col:
    :param match_val:
    :return:
    '''
    return df[df[col] == match_val]

if __name__ == '__main__':
    df = load_csv(sys.argv[1])
    #df2 = filter_by_string(df,'class','virginica')
    #df2 = filter_numeric_col_by_range(df,'sepal length',5.7,6.0)
    #df2 = filter_exact_match(df,'petal width',2.5)
    #df2 = filter_exact_match(df,'class','Iris-virginica')
