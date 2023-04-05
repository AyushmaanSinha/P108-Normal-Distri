import csv
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("Python/.CSV Files/MobileBrands.csv")
fig = ff.create_distplot([df["Mobile Brand"].tolist()], ["Avg Rating"])
fig.show()
