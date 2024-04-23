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


class Loan(models.Model):
    unique_user_id = models.UUIDField()  # A unique user identifier
    loanId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    loan_type = models.CharField(max_length=100)  # The type of loan
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)  # The loan amount in rupees
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  # The interest rate as a percentage
    term_period = models.PositiveIntegerField()  # The duration for repayment in months
    disbursement_date = models.DateField()  # The date of loan disbursal
