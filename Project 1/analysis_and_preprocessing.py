import numpy as np

def create_df(data_path):
    # input: the path of the csv file
    # output: data frame
    df = []
    return df

def nan_columns(df):
    # input: data frame
    # output: a list of names of columns that contain nan values in the data frame
    nancolumns = []
    return nancolumns

def categorical_columns(df):
    # input: data frame
    # output: a list of column names that contain categorical values in the data frame
    catcolumns = []
    return catcolumns

def replace_missing_features(df, nancolumns):
    # input: data frame, list of column names that contain nan values
    # output: data frame
    new_df1 = []
    return new_df1

def cat_to_num(new_df1, catcolumns):
    # input: data frame, list of categorical feature column names
    # output: data frame
    new_df2 = []
    return new_df2

def standardization(new_df2, labelcol):
    # input: data frame and name of the label column
    # output: scaled data frame
    new_df3 = []
    return new_df3


def my_train_test_split(new_df3, labelcol, test_ratio):
    # input: data frame, name of the label column and test data percentage
    # output: X_train, X_test, y_train, y_test
    np.random.seed(0) # DON'T ERASE THIS LINE

    X_train, X_test, y_train, y_test = [], [], [], []
    return X_train, X_test, y_train, y_test


def main(dataPath, testRatio, labelColumn):
    # input: the path of the csv file, test data percentage and name of the label column
    # output: X_train, X_test, y_train, y_test as numpy arrays

    X_train, X_test, y_train, y_test = [],[],[],[]
    return X_train, X_test, y_train, y_test
