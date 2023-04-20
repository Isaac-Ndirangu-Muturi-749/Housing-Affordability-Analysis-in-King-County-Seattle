# This function is designed to fill null values in a column with the mode of that column
def fun_mode_fill_null(df, column_name):
    # First calculate the mode value of a string
    mode_value = df[column_name].astype(str).mode()[0]
    # Then fill the null values with the mode value
    df[column_name].fillna(mode_value, inplace=True)
    return df

# This function is designed to fill null values in a column with the median of that column
def fun_median_fill_null(df, column_name):
    # First calculate the median value of a float
    median_value = df[column_name].astype(float).median()
    # Then fill the null values with the median value
    df[column_name].fillna(value = median_value, inplace=True)
    return df

# This function is designed to fill null values in a column with the median of that column, with the added benefit of removing figures that block propoer execution
def fun_median_fill_null_prob(df, column_name, problem):
    # First calculate, remove the troublsome figure, then convert to float, then calculate the median
    median_value = df[column_name].str.replace(problem, '').astype(float).median()
    # Then fill the null values with the median value
    df[column_name].fillna(median_value, inplace=True)
    return df

def fun_count_duplicates(df, column_name):
    """
    Count the number of duplicate values in a specified column of a DataFrame.

    Parameters:
        df (pandas.DataFrame): The DataFrame to search for duplicates.
        column_name (str): The name of the column to check for duplicates.

    Returns:
        int: The number of duplicate values in the specified column.
    """
    return df[column_name].duplicated().sum()

# This function is designed to drop duplicate values in a column
def fun_duplicates_drop(df, column_name):
    # Use the drop_duplicates method in a column, then retain the 1st duplicate in that column, then ensure the drop is permanent
    df.drop_duplicates(subset=[column_name], keep='first', inplace=True)
    return df

# This function is designed to replace values in a column with other values from a column containing similar values
def fun_replace_colvalues(df, columnnull, column_2):
    # Specify the column with null values,  the input the column with values you want to replace, then fill in the null values with values in the 2nd column
    df[columnnull] = df[columnnull].fillna(df[column_2].fillna(method = 'ffill'))
    return df

def fun_outlier_plot_box(df, column_name):
    """
    Create a box plot for a specified column of a Pandas DataFrame using Seaborn.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the column to plot.
        column_name (str): The name of the column to plot.

    Returns:
        None
    """
    sns.boxplot(x=df[column_name])