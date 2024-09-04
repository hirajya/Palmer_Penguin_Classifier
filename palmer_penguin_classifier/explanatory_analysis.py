def show_table(data):
    column_names = data.columns.tolist()

    print(f"The dataset has {data.shape[0]} rows and {data.shape[1]} columns.")
    print(f"The columns are: {column_names}")
    return data.head()