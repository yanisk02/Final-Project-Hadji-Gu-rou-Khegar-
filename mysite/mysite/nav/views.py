from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
from matplotlib.backends.backend_agg import FigureCanvasAgg

import pandas as pd
import numpy as np 
import plotly.express as px
import matplotlib.pyplot
import matplotlib.pyplot as plt

class MainPageView(TemplateView):
    template_name = 'nav/test2.html'
