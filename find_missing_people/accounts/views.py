from collections import defaultdict

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from contacts.models import Contact
from listings.models import MissingPerson

from .forms import RegistrationForm
from videos.models import ImagesFromVideo
from .tokens import account_activation_token


def register(request):
    if request.method == 'POST':
        regitseration_form = RegistrationForm(request.POST)

        if regitseration_form.is_valid():
            user = regitseration_form.save(commit=False)
            user.email = regitseration_form.cleaned_data['email']
            user.set_password(regitseration_form.cleaned_data['password'])
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Ativate Account'
            message = render_to_string('accounts/email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)})
            user.email_user(subject=subject, message=message)
            return redirect('pages:index')
    else:
        regitseration_form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': regitseration_form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except BaseException:
        return render(request, 'accounts/invalid.html')
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('accounts:dashboard')
    else:
        return render(request, 'accounts/invalid.html')


@login_required
def dashboard(request):
    if request.method == 'POST':
        if 'correct' in request.POST:
            missing_person_id, image_id = request.POST['correct'].split(',')
            request_info = MissingPerson.objects.get(id=missing_person_id)
            request_info.is_found = True
            request_info.save()

        elif 'wrong' in request.POST:
            missing_person_id, image_id = request.POST['wrong'].split(',')

        filtered_image = ImagesFromVideo.objects.order_by('-date').filter(user=request.user.id, missing_person=missing_person_id).get(id=image_id)
        filtered_image.delete()

    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    user_requests = MissingPerson.objects.order_by('-list_date').filter(user_id=request.user.id, is_accepted=True)
    user_taken_images = ImagesFromVideo.objects.order_by('-date').filter(user_id=request.user.id)
    image_dictionary = defaultdict(list)

    for image in user_taken_images:
        _id, missing_person_id, image_url = image.id, image.missing_person_id, image.photo.url
        image_dictionary[missing_person_id].append((image_url, _id))

    context = {
        'contacts': user_contacts,
        'requests': user_requests,
        'images': image_dictionary
    }
    return render(request, 'accounts/dashboard.html', context)
