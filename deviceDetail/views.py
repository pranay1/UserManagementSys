from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Device
from django.contrib.auth.decorators import login_required
from django.conf import settings
from auth0login.models import Profile
import datetime



@login_required
def index(request):
    user = request.user
    username = user.username
    firstname = user.first_name
    lastname = user.last_name
    email = user.email
    print(username, firstname, lastname, email, "here", Profile.username)
    devices = Device.objects.filter(username=user)
    count=1
    print(devices)
    return render(request, 'list_device1.html', {'devices': devices ,'count':count})



@login_required
def create_device(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST['name']
        type = request.POST['type']
        parameters = request.POST['parameters']
        print(type)
        #quantity = request.POST['quantity']
        created_device = Device(username=user,
                                name=name,
                                type=type,
                                parameters=parameters)

        created_device.save()
        return redirect('index')
    else:
        return render(request, 'device_detail_form1.html')



@login_required
def display_device_info(request, id):
    fetched_device = Device.objects.get(id=id)
    print(fetched_device.id)
    id = fetched_device.id
    name = fetched_device.name
    type = fetched_device.type
    parameters = fetched_device.parameters
    #quantity = fetched_device.quantity
    #id = fetched_device.id
    return render(request, 'display_device_info1.html',
                  {'id': id,
                   'name': name,
                   'type': type,
                   'parameters': parameters})



#@login_required
#def update_device_info(request):
#    return HttpResponse("update called")


@login_required
def delete_device_info(request, id):
    fetched_device = Device.objects.get(id=id)
    fetched_device.delete()
    return redirect('index')
