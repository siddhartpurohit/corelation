import plotly.express as px
import csv
import numpy as np

def getDataSource(b):
    size = []
    time = []
    with open(b) as csvfile:
        cReader = csv.DictReader(csvfile)
        for i in cReader:
            size.append(float(i["Size of TV"]))
            time.append(float(i["Average time spent watching TV in a week (hours)"]))
    return {"x":size,"y":time}

def findCorrelation(ds):
    c = np.corrcoef(ds["x"],ds["y"])
    print("corelation is :",c[0,1])

def setup():
    dp = "tv.csv"
    se = getDataSource(dp)
    findCorrelation(se)

setup()

# not corelated because number is close to 0s