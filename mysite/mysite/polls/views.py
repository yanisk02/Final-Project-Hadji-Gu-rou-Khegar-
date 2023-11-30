from django.http import HttpResponse
from django.shortcuts import render

#%% modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
import plotly.express as px
import plotly.graph_objects as go
import io
import urllib, base64

# hide warnings
import warnings
warnings.filterwarnings('ignore')

from urllib.request import urlopen
import json

data = pd.read_csv("SeoulBikeData.csv",encoding='iso-8859-1')
data['Date'] = pd.to_datetime(data['Date'],format="%d/%m/%Y")
data_num = data.select_dtypes(include=['int64', 'float64'])
data_corr= data_num.corr()


#%% views
def index1(request):
        plt.figure(figsize=(20, 20))
        sns.heatmap(data_corr, cmap='coolwarm', linewidths=0.1, annot=True, linecolor='black', fmt=".2f")
        plt.title("Correlation matrix")
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        fig = plt.figure(figsize=(20, 5))

        for index, column in enumerate(data_num.columns):
            plt.subplot(3, 5, index + 1)
        
            sns.histplot(data_num[column], kde=True) 

            feature = data_num[column]
            ax = fig.gca()
        
            ax.axvline(feature.mean(), color='#ff033e', linestyle='dashed', linewidth=2)  
            ax.axvline(feature.median(), color='#00ffff', linestyle='dashed', linewidth=2)

            plt.title(f'{column.title()}')
            plt.tight_layout()
        Buffer = io.BytesIO()
        plt.savefig(Buffer, format='png')
        Buffer.seek(0)
        image_base64_2 = base64.b64encode(Buffer.read()).decode('utf-8')
        context = {"image_base64": image_base64,"image_base64_2": image_base64_2}
        return render(request, "progress.html", context)

def index2(request):
    context={}
    return render(request, "About_Us.html", context)

def index3(request):
    context={}
    return render(request, "Camembert.html", context)