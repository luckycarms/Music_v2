

def null_check(df):
    """ Checking the dataframe for null/NaN values.
    
    Parameters:
    df: The DataFrame to check
   
     Returns:
    boolean: True if present otherwise False"""
    
    return df.isnull().any().any()



def clean(df):
    """Clean the DataFrame by dropping rows with any null/NaN values.

    Parameters:
    df: The DataFrame to clean

    Returns:
    pd.DataFrame: A new DataFrame without NaN values, with index reset
    """
    df_cleaned = df.dropna().reset_index(drop=True)
    return df_cleaned 



