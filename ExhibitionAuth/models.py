from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
# visitors data in here
class Visitor(models.Model):
    visitor_user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    visitor_name = models.CharField(max_length=100)

    def __str__(self):
        return self.visitor_name


# exhibitor data are here
class Exhibitor(models.Model):
    exhibitor_user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    exhibitor_company_name = models.CharField(max_length=100)
    exhibitor_address = models.CharField(max_length=300)
    exhibitor_mobile_number = models.CharField(max_length=20)

    def __str__(self):
        return self.exhibitor_company_name
