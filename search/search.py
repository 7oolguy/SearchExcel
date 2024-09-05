import pandas as pd

def search_whole_sheet(file_path, search_value, sheet_name=None):
    """
    Search for a value across all columns in a DataFrame and return rows where the value is found.

    :param df: DataFrame to search in
    :param search_value: Value to search for
    :return: DataFrame containing rows where the search value is found
    """
    try:
        # Load the Excel file into a DataFrame
        if sheet_name:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        else:
            df = pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return pd.DataFrame()

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

    return search_results.values.tolist()
