from django.shortcuts import render
from django.views import View
from django.views import generic
from .models import MissingPeople
from .forms import RequestForm

# Create your views here.


class Web_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'web_board/web_board_list.html'
        missing_people = MissingPeople.objects.all()
        return render(request, template_name, {"missing_people" : missing_people})


def check_board(request):
    template_name = 'web_board/web_board_success.html'
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            request_form = form.save(commit=False)
            request_form.save()
            message = "Your request has been sent successfully."
            return render(request, template_name, {"message": message})
    else:
        template_name = 'web_board/web_board_request.html'
        form = RequestForm
        return render(request, template_name, {"form": form})