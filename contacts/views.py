from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.utils import timezone

from contacts.models import Contact
from django.contrib.auth.models import User
from listings.models import MissingPerson


def contact(request):
    if request.method == 'POST':
        request_info = request.POST
        missing_person_id = request_info['missing_person_id']
        name = request_info['name']
        phone = request_info['phone']
        message = request_info['message']
        user_id = request_info['user_id']
        requestor_email = request_info['requestor_email']
        date = request_info['date']
        user = User.objects.get(id=user_id)
        missing_person = MissingPerson.objects.get(id=missing_person_id)
        has_contacted = Contact.objects.all().filter(missing_person=missing_person_id, user=user_id)

        if has_contacted:
            messages.error(request, 'You have already sent information')
        else:
            contact = Contact(missing_person=missing_person, from_name=name, email=requestor_email,
                    phone=phone, message=message, last_seen=date, contact_date=timezone.now(), user=user)
            contact.save()
            send_mail(
                'Find Missing People',
                'Someone sent information about %s from %s.' %(missing_person.name, name),
                '' ,  # from email
                [requestor_email, ''],  # to email
                fail_silently = False
            )

            messages.success(request, 'Success to send information.')

        return redirect('/listings/' + missing_person_id)
