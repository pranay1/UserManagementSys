from django.contrib import admin
from .models import Profile

# Register your models here.

#admin.site.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = [('username'), 'firstname',
                    'lastname', 'email', 'phone', 'address', 'profession','city', 'state', 'country']
    fields = [('username'), 'firstname', 'lastname', 'email', 'phone', 'address', 'profession','city', 'state', 'country']
    readonly_fields = ['username']


admin.site.register(Profile, ProfileAdmin)
