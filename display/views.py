from django.shortcuts import render
import pandas as pd
from plotly.offline import plot
import plotly.express as px

from upload.views import getFilesNames
# Create your views here.
functionNames = [
    "MAX",
    "MIN",
    "SUM"
]
def display(request):
    context = {"data":getFilesNames(),"functionNames":functionNames}
    df = pd.read_csv('static\california_housing_test.csv')
    fig = px.bar(
        x=df["longitude"], y=df["latitude"]
    )
    gantt_plot = plot(fig,output_type="div")
    context["plot_div"] = gantt_plot
    return render(request,'display.html',context)