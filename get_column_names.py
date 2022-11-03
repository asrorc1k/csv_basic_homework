#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    a=[]
    for i in data:
        a.append(i.split())
    print(a)
# Read the csv file
f = open('data.csv').read().split()
print(get_column_names(f))
