import pandas as pd

def Remove_Outliers(df: pd.DataFrame, cols):
    """
    Removes outliers from a single numeric column using the IQR method.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame
        col (str): Column name to apply outlier removal
    
    Returns:
        pd.DataFrame: Filtered DataFrame without outliers in that column
    """

    Q1 = df[cols].quantile(0.25)
    Q3 = df[cols].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    
     
    df_cleaned = df[(df[cols] >= lower) & (df[cols] <= upper)]

    return df_cleaned  