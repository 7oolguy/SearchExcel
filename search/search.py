import pandas as pd

def search_whole_sheet(df, search_value):
    """
    Search for a value across all columns in a DataFrame and return rows where the value is found.
    
    :param df: DataFrame to search in
    :param search_value: Value to search for
    :return: DataFrame containing rows where the search value is found
    """
    if df.empty:
        print("The DataFrame is empty.")
        return pd.DataFrame()
    
    if not search_value:
        print("Search term is empty.")
        return pd.DataFrame()
    
    # Convert the search value to string for comparison
    search_value = str(search_value).lower()
    
    # Create a boolean DataFrame where True represents matches
    boolean_df = df.apply(lambda col: col.astype(str).str.contains(search_value, case=False, na=False))
    
    # Filter rows where any cell contains the search value
    search_results = df[boolean_df.any(axis=1)]
    
    return search_results