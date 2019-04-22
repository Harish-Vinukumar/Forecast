from django.shortcuts import render
from .forms import ForeCast
import requests as req


def forecast(request):
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    if request.method == 'POST':
        form = ForeCast(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            url = api_address + city
            json_data = req.get(url).json()
            description = str(json_data['weather'][0]['description']).capitalize()
            temperature = str(json_data['main']['temp']) + ' deg F'
            humidity = str(json_data['main']['humidity'])
            pressure = str(json_data['main']['pressure']) + ' pascal'
            context = {'city': city.upper(), 'description': description, 'temperature': temperature, 'humidity': humidity,
                       'pressure': pressure}
            return render(request, 'Forecast/Weather.html', context=context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ForeCast()

    return render(request, 'Forecast/Forecast.html', {'form': form})
