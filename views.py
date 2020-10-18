from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request, 'home.html')

def result(request):

    pipe_ls = joblib.load('final_model.sav')
    
    ls = []

    ls.append(request.GET['Brand'])
    ls.append(request.GET['Model'])
    ls.append(request.GET['Fuel type'])
    ls.append(request.GET['Transmission'])
    ls.append(request.GET['Condition'])
    ls.append(request.GET['First Registration Year'])
    ls.append(request.GET['Milleage (kms)'])
    ls.append(request.GET['Engine Power (PS)'])
    ls.append(request.GET['Production_Year'])
    
    price = pipe_ls.predict([ls])

    return render(request, 'result.html', {'price':price})