__author__ = 'Ed Cannon'

import pandas as pd
from filter_df import load_csv
import sys

def sort_by_one_column(df,col,ascending=False):
    '''

    :param df: input data frame to sort
    :param col: column to sort by
    :param ascending: values to be sorted in ascending order?
    :return: sorted data frame
    '''
    return df.sort([col], ascending=ascending)

if __name__ == '__main__':
    df = load_csv(sys.argv[1])
    #df2 = sort_by_one_column(df,'sepal length')
    #print df2.head()