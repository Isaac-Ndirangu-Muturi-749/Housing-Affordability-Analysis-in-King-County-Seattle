# This function is designed to fill null values in a column with the median of that column
def fun_median_fill_null(df, column_name):
    # First calculate the median value of a float
    median_value = df[column_name].astype(float).median()
    # Then fill the null values with the median value
    df[column_name].fillna(value = median_value, inplace=True)
    return df