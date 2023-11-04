# contractor/models.py

from django.db import models
from django.conf import settings

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Contractor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    services_offered = models.ManyToManyField(Service)
    # Add additional fields as needed
    business_license = models.FileField(upload_to='licenses')
    insurance_document = models.FileField(upload_to='insurances')
    tax_document = models.FileField(upload_to='tax_documents')

    def __str__(self):
        return self.company_name

# You can add more models as needed for your application.
