def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    return data.split()[0]
# Read the csv file
f = open('data.csv').read()

print(get_first_column(f))
 