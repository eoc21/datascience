__author__ = 'Ed Cannon'

import pandas as pd
from filter_df import load_csv
import sys
from collections import OrderedDict

def sort_by_one_column(df,col,ascending=False):
    '''

    :param df: input data frame to sort
    :param col: column to sort by
    :param ascending: values to be sorted in ascending order?
    :return: sorted data frame
    '''
    return df.sort([col], ascending=ascending)

def sort_by_multiple_columns(df,cols_order):
    '''
    Sorts a data frame on multiple columns
    :param df: input data frame to sort
    :param cols_order: sorted dictionary of columns and whether to sort
    in ascending/descending fashion
    :return: sorted data frame
    '''
    if len(df.columns) >= len(cols_order.items()):
        return df.sort(cols_order.keys(), ascending=cols_order.values())
    else:
        print "number of columns in ordered dictionary > cols in data frame!"
        return df

if __name__ == '__main__':
    df = load_csv(sys.argv[1])
    #od = OrderedDict()
    #od.__setitem__("sepal length",0)
    #od.__setitem__("sepal width",0)
    #res = sort_by_multiple_columns(df,od)
