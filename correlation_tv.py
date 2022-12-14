from statistics import correlation
import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path)as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="size",y="average_time")
        fig.show()
def getDataSource(data_path):
    size=[]
    average_time=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            size.append(float(row["size"]))
            average_time.append(float(row["average_time"]))
            return{"x":size,"y":average_time}
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between size of tv vs average time spent :- \n--->",correlation[0,1])
data_path="tvdata.csv"
datasource=getDataSource(data_path)
findCorrelation(datasource)
plotFigure(data_path)

    