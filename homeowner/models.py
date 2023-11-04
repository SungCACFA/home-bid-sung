# homeowner/models.py

from django.db import models
from django.conf import settings

class Homeowner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    preferred_contact_method = models.CharField(max_length=50, choices=[
        ('email', 'Email'),
        ('phone', 'Phone Call'),
        ('text', 'Text Message'),
        # Add more contact methods if needed
    ])
    email = models.EmailField()
    number_of_bathrooms = models.IntegerField()
    has_basement = models.BooleanField(default=False)
    property_type = models.CharField(max_length=50, choices=[
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('townhouse', 'Townhouse'),
        # Add more property types if needed
    ])

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Property(models.Model):
    homeowner = models.ForeignKey(Homeowner, related_name='properties', on_delete=models.CASCADE)
    address = models.TextField()
    image = models.ImageField(upload_to='properties')  # Ensure Pillow is installed
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Property of {self.homeowner.user.get_full_name() or self.homeowner.user.username}"
