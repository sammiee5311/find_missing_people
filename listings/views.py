import datetime

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from .choices import (end_year_choices, sex_choices, start_year_choices,
                      state_choices)
from .models import MissingPeople


def listings_all(request):
    listings = MissingPeople.objects.order_by('-list_date').filter(is_private=False, is_found=False, is_accepted=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def detail(request, listing_id):
    listing = get_object_or_404(MissingPeople, pk=listing_id)
    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    query_list = MissingPeople.objects.order_by('-list_date').filter(is_accepted=True)
    start_year = datetime.date(int(2000), 1, 1)
    end_year = datetime.datetime.now()

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_list = query_list.filter(state__iexact=state)

    if 'sex' in request.GET:
        sex = request.GET['sex']
        if sex:
            query_list = query_list.filter(sex__iexact=sex)
    
    if 'start_year' in request.GET:
        start_year = request.GET['start_year']
        if start_year:
            start_year = datetime.date(int(start_year), 1, 1)        

    if 'end_year' in request.GET:
        end_year = request.GET['end_year']
        print(end_year)
        if end_year:
            end_year = datetime.date(int(end_year), 12, 31)

    query_list = query_list.filter(list_date__range=(start_year, end_year))       
    context = {
        'state_choices': state_choices,
        'sex_choices': sex_choices,
        'start_year_choices': start_year_choices,
        'end_year_choices': end_year_choices,
        'listings': query_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)
