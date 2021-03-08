# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from re import X
import pandas as pd
import plotly.express as px
from plotly.offline import plot
from app.plotly_functions import bar_chart
from app.plotly_functions import line_chart
import os

path = os.path.dirname(__file__)
data = pd.read_csv(path + '/data.csv')

def index(request):
    #escribo una cosa aqui
    context = {'title': 'Majority Report Medellín',
               'subtitle': 'Bienvenidos',
               'tab_1_title':"Acerca de",
               'tab_1_text': 'Esta es una página donde encontrará una forma de visualizar los índices de criminalidad en la ciudad de Medellín de manera interactiva',
               'tab_2_title':"Instrucciones",
               'tab_2_text': "Acá explicamos otra cosa",
               'tab_3_title':"Contacto",
               'tab_3_text': "Estoy inventando",
               'chart_1_title': "Cantidad de hurtos a personas por sexo de la víctima desde 2003",
               'chart_1':"",
               'chart_2_title':"Cantidad de hurtos a personas mes a mes desde el 2003",
               'chart_2':""}
    context['chart_1'] = bar_chart(data, 'sexo', 'cantidad')
    context['chart_2'] = line_chart(data, 'año', 'mes', 'cantidad')
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))


def medellincharts(request):
    #creo key en context que contengan cada una de las fgráficas
    context = {'chart_1_title': "Cantidad de hurtos por año desde el 2003",
               'chart_1':"",
               'chart_2_title':"Cantidad de hurtos por barrio desde el 2003",
               'chart_2':"",
               'chart_3_title': "Cantidad de hurtos por arma utilizada",
               'chart_3':"",
               'chart_4_title': "Cantidad de hurtos por hora durante los días de la semana",
               'chart_4': "",
               'chart_5_title': "Cantidad de hurtos por semana durante el año desde el 2003",
               'chart_5': "",
               'chart_6_title': "Cantidad de hurtos por hora desde el 2003",
               'chart_6': "",
               'chart_7_title': "Cantidad de hurtos por modalidad empleada",
               'chart_7': ""}
    #ex: context['bar_chart_1'] = bar_chart(data, 'seguridad.sexo', 'seguridad.cantidad')
    context['chart_1'] = bar_chart(data, 'año', 'cantidad')
    context['chart_2'] = bar_chart(data, 'nombre_barrio', 'cantidad')
    context['chart_3'] = bar_chart(data, 'arma_medio', 'cantidad')
    context['chart_4'] = line_chart(data, 'dia', 'hora', 'cantidad')
    context['chart_5'] = bar_chart(data, 'semana', 'cantidad')
    context['chart_6'] = bar_chart(data, 'hora', 'cantidad')
    context['chart_7'] = bar_chart(data, 'modalidad', 'cantidad')
    context['segment'] = 'medellincharts.html'

    html_template = loader.get_template( 'medellincharts.html')
    return HttpResponse(html_template.render(context, request))

#@login_required(login_url="/login/")
#def pages(request):
#    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
#    try:

#        load_template      = request.path.split('/')[-1]
#        context['segment'] = load_template

#        html_template = loader.get_template( load_template )
#        return HttpResponse(html_template.render(context, request))

#    except template.TemplateDoesNotExist:

#        html_template = loader.get_template( 'page-404.html' )
#        return HttpResponse(html_template.render(context, request))

#    except:
#
#        html_template = loader.get_template( 'page-500.html' )
#        return HttpResponse(html_template.render(context, request))
