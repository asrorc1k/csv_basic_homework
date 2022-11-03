def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
reader = csv.reader(f)
a=0
for row in reader:
    a+=1
    return a
# Read the csv file
f = open('data.csv').read().split()
