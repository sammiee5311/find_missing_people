from django.contrib import messages
from django.core.serializers import serialize
from django.shortcuts import render
from django.utils import timezone
from geopy.geocoders import Nominatim

from listings.choices import (end_year_choices, sex_choices,
                              start_year_choices, state_choices)
from listings.models import MissingPerson
from requestors.models import Requestor

geolocator = Nominatim(user_agent="find_missing_people")


def index(request):
    listings = MissingPerson.objects.order_by('-list_date').filter(is_found=False, is_private=False, is_accepted=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'sex_choices': sex_choices,
        'start_year_choices': start_year_choices,
        'end_year_choices': end_year_choices
    }

    return render(request, 'pages/index.html', context)


def map(request):
    requestors = Requestor
    query_list = MissingPerson.objects.order_by('-list_date')

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)
            pass

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)
            pass
    
    query_list = serialize('json', query_list, fields=['name', 'address', 'city', 'state', 'lat', 'lng'])

    context = {
        'requestors': requestors,
        'listing': query_list,
        'state_choices': state_choices,
    }

    return render(request, 'pages/map.html', context)


def request(request):
    global geolocator

    if request.method == 'POST':
        request_info = request.POST
        name = request_info['name']
        sex = request_info['sex'] if 'sex' in request_info else None
        age = request_info['age']
        city = request_info['city']
        image = request.FILES['image'] if 'image' in request_info else None
        state = request_info['state'] if 'state' in request_info else None
        address = request_info['address']
        is_private = True if 'private' in request_info else False
        date = request_info['date']
        list_date = timezone.now()
        description = request_info['description']

        location = geolocator.geocode(address)
        longitude, latitude = round(location.longitude, 3), round(location.latitude, 3)

        if not sex or not state:
            messages.error(request, 'You should Choose Sex and State both.')
        else:
            MissingPerson.objects.create(name=name, address=address,
                                         city=city, state=state, sex=sex, age=age, photo_main=image, description=description,
                                         lng=longitude, lat=latitude, is_private=is_private, is_found=False,
                                         missing_date=date, list_date=list_date, is_accepted=False, user=request.user)
            messages.success(request, 'Reqeust Successfully')

    context = {
        'state_choices': state_choices,
        'sex_choices': sex_choices,
    }

    return render(request, 'pages/request.html', context)
