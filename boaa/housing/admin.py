from django.contrib import admin
from housing.models import Apartment, Profile, Ticket

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ["address", "owner"]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["owner", "first_name", "last_name", "address"]
