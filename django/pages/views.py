from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import sex_choices, state_choices, start_year_choices, end_year_choices
from listings.choices import state_choices
from django.contrib import messages, auth
from django.core.serializers import serialize
from datetime import datetime

from listings.models import MissingPeople
from requestors.models import Requestor
from django.contrib.auth.models import User

import json

def index(request):
    listings = MissingPeople.objects.order_by('-list_date').filter(is_found=False, is_private=False)[:3]

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
    query_list = MissingPeople.objects.order_by('-list_date')

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
    if request.method == 'POST':
        request_info = request.POST
        name = request_info['name']
        sex = request_info['sex'] if 'sex' in request_info else None
        age = request_info['age']
        city = request_info['city']
        image = request.FILES['image']
        state = request_info['state'] if 'state' in request_info else None
        address = request_info['address']
        longitude = request_info['longitude']
        latitude = request_info['latitude']
        date = request_info['date']
        list_date = datetime.today().strftime('%Y-%m-%d')
        description = request_info['description']

        if not sex or not state:
            messages.error(request, 'You should Choose Sex and State both.')
        else:
            MissingPeople.objects.create(name=name, address=address, 
            city=city, state=state, sex=sex, age=age, photo_main=image, description=description, lng=longitude, lat=latitude, is_private=False, is_found=False,
            missing_date=date, list_date=list_date, is_accepted=False, user=request.user)
            messages.success(request, 'Reqeust Successfully')

    context = {
        'state_choices': state_choices,
        'sex_choices': sex_choices,
    }

    return render(request, 'pages/request.html', context)