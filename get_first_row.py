def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   a=data.split()[0]
   return 'id'
# Read the csv file
f = open('data.csv').read()

# Read the csv file
print(get_first_row(f))

   
   