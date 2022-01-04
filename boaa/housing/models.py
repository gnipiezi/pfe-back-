from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    owner = models.ForeignKey(User, editable=False, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    address = models.TextField()


class Apartment(models.Model):
    owner = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    site = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    address = models.TextField()
    created_date = models.DateTimeField(auto_created=True)
    last_updated = models.DateTimeField(auto_now=True)


TicketStatus = [
    ("OPEN", "Open"),
    ("PROGRESS", "In progress"),
    ("CLOSED", "Closed")
]


class Ticket(models.Model):
    owner = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_created=True)
    status = models.CharField(
        max_length=8,
        choices=TicketStatus,
        default="OPEN"
    )
