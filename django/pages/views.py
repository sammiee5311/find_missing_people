from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import sex_choices, state_choices, start_year_choices, end_year_choices
from listings.choices import state_choices
from django.core.serializers import serialize

from listings.models import Listing
from requestors.models import Requestor

import json

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_found=False, is_private=False)[:3]

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
    query_list = Listing.objects.order_by('-list_date')

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)


    query_list = serialize('json', query_list, fields=['name', 'address', 'city', 'state', 'lat', 'lng'])

    context = {
        'requestors': requestors,
        'listing': query_list,
        'state_choices': state_choices,
    }

    return render(request, 'pages/map.html', context)