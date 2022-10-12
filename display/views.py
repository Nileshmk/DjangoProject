from django.shortcuts import render
import pandas as pd
from plotly.offline import plot
import plotly.express as px
# Create your views here.
files = [
    "Data file 01",
    "Data file 02",
    "Data file 03",
    "Data file 04",
    "Data file 05",
]
functionNames = [
    "MAX",
    "MIN",
    "SUM"
]
def display(request):
    context = {"data":files,"functionNames":functionNames}
    df = pd.read_csv('static\california_housing_test.csv')
    fig = px.bar(
        x=df["longitude"], y=df["latitude"]
    )
    gantt_plot = plot(fig,output_type="div")
    context["plot_div"] = gantt_plot
    return render(request,'display.html',context)