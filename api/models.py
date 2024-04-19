from django.db import models

# Create your models here.

'''
    post /api/register-user/
    post /api/apply-loan/
    post /api/make-payment/
    get /api/get-statement/
'''

import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    aadhar_id = models.CharField(max_length=50, null = False, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=False, unique=True)
    annual_income = models.CharField(max_length=50)