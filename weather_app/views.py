from django.shortcuts import render , redirect

# Create your views here.
from .models import city
from .forms import CityForm
import requests


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=b06cb360376dbe3856ccd8695fa03fa4'
    err_msg = ''
    message = ''
    message_class = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = city.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                print(r)
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = "City doesnt exist"
            else:
                err_msg = "City already exist in the database!"
        if err_msg :
            message = err_msg
            message_class = 'alert-danger'
        else:
            message = 'City added successfully!'
            message_class = "alert-success"
    
    print(err_msg)
    form = CityForm()
    cities = city.objects.all()

    weather_data = []

    for citi in cities:

        r = requests.get(url.format(citi)).json()
        city_weather  = {
            'city' : citi.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {
        'weather_data' : weather_data, 
        'form':form,
        'message':message,
        'message_class':message_class
    }


    return render(request , 'index.html' ,  context)


def about(request) :
    return render(request,'about.html')

    
def delete_city(request, city_name):
    city.objects.get(name=city_name).delete()
    return redirect('home')

def help(request):
    return render(request,'help.html')
