from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
from .models import Profile
from django.shortcuts import redirect, render


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect(check_user_info)
    else:
        return render(request, 'index1.html')


@login_required()
def check_user_info(request):
    user = request.user
    if not Profile.objects.filter(username=user).exists():
        create_user = Profile(username=user)
        create_user.save()
        print('New user created in extended profile table')
        return redirect(get_user_info)
    return redirect(get_user_info)


@login_required
def get_user_info(request):
    current_user = request.user
    current_user_profile = Profile.objects.get(username=current_user)
    username = current_user_profile.username.username
    firstname = current_user_profile.firstname
    lastname = current_user_profile.lastname
    email = current_user_profile.email
    phone = current_user_profile.phone
    mandatory_fields = {'firstname': firstname, 'lastname': lastname, 'phone': phone, 'email': email, }
    for key, value in mandatory_fields.items():
        if value == '':
            return redirect(edit_user_info)
    return render(request, 'display_info1.html', {'username': username,
                                                  'firstname': firstname,
                                                  'lastname': lastname,
                                                  'phone': phone,
                                                  'email': email, })


@login_required
def edit_user_info(request):
    print("inside edit function")
    current_user = request.user
    current_user_profile = Profile.objects.get(username=current_user)
    username = current_user_profile.username.username
    firstname = current_user_profile.firstname
    lastname = current_user_profile.lastname
    email = current_user_profile.email
    phone = current_user_profile.phone
    address = current_user_profile.address
    profession = current_user_profile.profession
    city = current_user_profile.city
    state = current_user_profile.state
    country = current_user_profile.country
    return render(request, 'form1.html', {'username': username,
                                          'firstname': firstname,
                                          'lastname': lastname,
                                          'phone': phone,
                                          'email': email,
                                          'address': address,
                                          'profession': profession,
                                          'city': city,
                                          'state': state,
                                          'country': country,
                                          })


@login_required
def update_user_info(request):
    if request.method == 'POST':
        current_user = request.user
        current_user_profile = Profile.objects.get(username=current_user)
        if not request.POST['firstname'] == "":
            current_user_profile.firstname = request.POST['firstname']
            current_user_profile.save(update_fields=['firstname'])
            current_user.first_name = current_user_profile.firstname
            current_user.save(update_fields=["first_name"])
        if not request.POST['lastname'] == "":
            current_user_profile.lastname = request.POST['lastname']
            current_user_profile.save(update_fields=['lastname'])
            current_user.last_name = current_user_profile.lastname
            current_user.save(update_fields=["last_name"])
        if not request.POST['email'] == "":
            current_user_profile.email = request.POST['email']
            current_user_profile.save(update_fields=['email'])
            current_user.email = current_user_profile.email
            current_user.save(update_fields=["email"])
        if not request.POST['phone'] == "":
            current_user_profile.phone = request.POST['phone']
            current_user_profile.save(update_fields=['phone'])
        if not request.POST['address'] == "":
            current_user_profile.address = request.POST['address']
            current_user_profile.save(update_fields=['address'])
        if not request.POST['profession'] == "":
            current_user_profile.profession = request.POST['profession']
            current_user_profile.save(update_fields=['profession'])
        if not request.POST['city'] == "":
            current_user_profile.city = request.POST['city']
            current_user_profile.save(update_fields=['city'])
        if not request.POST['state'] == "":
            current_user_profile.state = request.POST['state']
            current_user_profile.save(update_fields=['state'])
        if not request.POST['country'] == "":
            current_user_profile.country = request.POST['country']
            current_user_profile.save(update_fields=['country'])

        return redirect(get_user_info)


@login_required
def delete_user_info(request):
    current_user = request.user
    current_user_profile = Profile.objects.get(username=current_user)
    current_user_profile.delete()
    return redirect('/admin')


@login_required
def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)
