import csv

def getCSVData(filename):
    rows=[]
    datFile = open(filename,"r")
    reader = csv.reader(datFile)
    # Skip first line
    next(reader)
    for row in reader:
        rows.append(row)
    return rows