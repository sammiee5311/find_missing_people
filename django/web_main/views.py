from django.shortcuts import render

from django.views import View
from django.views import generic

from .models import MissingPeople

# Create your views here.


class Web_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'web_main/index.html'
        missing_people = MissingPeople.objects.all()
        return render(request, template_name, {"missing_people": missing_people})


class Web_main_detail(generic.DetailView):
    model = MissingPeople
    template_name = 'web_main/web_main_detail.html'
    context_object_name = 'missing_people'
