from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from contacts.models import Contact

def contact(request):
    if request.method == 'POST':
        request_info = request.POST
        missing_person_name = request_info['missing_person_name']
        listing_id = request_info['listing_id']
        name = request_info['name']
        phone = request_info['phone']
        message = request_info['message']
        user_id = request_info['user_id']
        requestor_email = request_info['requestor_email']
        date = request_info['date']

        has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
        
        if has_contacted:
            messages.error(request, 'You have already sent information')
        else:
            contact = Contact(missing_person_name=missing_person_name, listing_id=listing_id, from_name=name, email=requestor_email, phone=phone, message=message, last_seen=date, user_id=user_id)
            contact.save()
            # send_mail(
            #     'Find Missing People',
            #     'Someone sent information about %s from %s.' %(missing_person_name, name),
            #     '' , # from email
            #     [requestor_email, ''], # to email
            #     fail_silently = False
            # )

            messages.success(request, 'Success to send information.')

        return redirect('/listings/'+listing_id)
