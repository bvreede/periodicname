import csv

def _read_periodictable():
    """Read the periodic table file and return the data as a nested list"""
    periodictable = open('periodicname/data/periodicdata.csv')
    periodictable_csv = csv.reader(periodictable)
    periodictable_list = list(periodictable_csv)
    return(periodictable_list) 

def get_elements():
    """Return the elements of the periodic table as a list"""
    periodictable = _read_periodictable()
    elements = [el[3] for el in periodictable[1:]]
    return elements