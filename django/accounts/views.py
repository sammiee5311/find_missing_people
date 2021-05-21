from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from listings.models import MissingPeople
from .models import ImagesFromVideo

from collections import defaultdict

def register(request):
    if request.method == 'POST':
        request_info = request.POST
        first_name = request_info['first_name']
        last_name = request_info['last_name']
        username = request_info['username']
        email = request_info['email']
        password = request_info['password']
        password_confirm = request_info['password_confirm']
        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register') 
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    # auth.login(request, user)
                    messages.success(request, 'Register Successfully')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not macth')
            return redirect('register')
    return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        request_info = request.POST
        username, password = request_info['username'], request_info['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            messages.success(request, 'Login Succeeded')
            return redirect('index')
        else:
            messages.error(request, 'Login Failed')
            return redirect('dash')
    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged Out Succeeded')
    return redirect('index')

def dashboard(request):
    if request.method == 'POST':
        if 'correct' in request.POST:
            missing_person_id, image_id = request.POST['correct'].split(',')
            request_info = MissingPeople.objects.get(id=missing_person_id)
            request_info.is_found = True
            request_info.save()

        elif 'wrong' in request.POST:
            missing_person_id, image_id = request.POST['wrong'].split(',')

        filtered_image = ImagesFromVideo.objects.order_by('-date').filter(user_id=request.user.id, missing_person_id=missing_person_id).get(id=image_id)
        filtered_image.delete()

    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    user_requests = MissingPeople.objects.order_by('-list_date').filter(user_id=request.user.id, is_accepted=True)
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