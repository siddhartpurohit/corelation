
import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    icSales = []
    temp = []
    with open( data_path) as c:
        cReader = csv.DictReader(c)
        for i in cReader:
            temp.append( float( i["Temperature"]  ) )
            icSales.append( float( i["Ice-cream Sales"]  ) )
    return { "x" : temp , "y" : icSales} 

def findCorrelation( ds ):
    #correlation coefficient
    c = np.corrcoef( ds["x"] , ds["y"] )
    print("Correlation is : "  ,  c[0,1])


def setup():
    dp = "iceCream.csv"
    ds = getDataSource(dp)
    findCorrelation(ds )

setup()


#closely corelated because value is 0.95