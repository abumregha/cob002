from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_slug, validate_email, RegexValidator


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_Created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
class NewAccountData(models.Model):
    STATUS = (
        ('not Started', 'not Started'),
        ('Approved', 'Approved'),
        ('Submitted', 'Submitted'),
        ('Please Revise', 'Please Revise'),
        ('Unfinished', 'Unfinished'),

    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    SALARY = (
        ('Under 12,000 per year', 'Under 12,000 per year'),
        ('From 12,000 to 25,000 per year', 'From 12,000 to 25,000 per year'),
        ('From 25,000 to 35,000 per year', 'From 25,000 to 35,000 per year'),
        ('From 35,000 to 50,000 per year', 'From 35,000 to 55,000 per year'),
        ('Above 50,000 per year', 'Above 50,000 per year'),
    )

    #customer = models.OneToOneField(Customer, null=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    First_Name_Arabic = models.CharField(max_length=40, blank=True, null=True)
    Middle_Name_Arabic = models.CharField(max_length=40, blank=True, null=True)
    Last_Name_Arabic = models.CharField(max_length=40, blank=True, null=True)
    First_Name_English = models.CharField(max_length=40, blank=True, null=True)
    Middle_Name_English = models.CharField(max_length=40, blank=True, null=True)
    Last_Name_English = models.CharField(max_length=40, blank=True, null=True)
    Birth_dt = models.DateField(blank=True, null=True)
    PlaceOFBirth = models.CharField(max_length=40, blank=True, null=True)
    Gender = models.CharField(max_length=20, blank=True, null=True, choices=GENDER)
    MartialStatus = models.CharField(max_length=40, blank=True, null=True)
    Home_Address = models.CharField(max_length=40, blank=True,null=True)
    City = models.CharField(max_length=40, default='Tripoli')
    Country = models.CharField(max_length=40, default='Libya')
    Nationality = models.CharField(max_length=40, default='Libyan')
    CountryOfBirth = models.CharField(max_length=40, default='Libya')
    date_Created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    Email = models.EmailField(max_length=100, blank=True, null=True, unique=True, validators=[validate_email])
    EmployerName = models.CharField(max_length=100, blank=True, null=True)
    Position = models.CharField(max_length=100, blank=True, null=True)
    EmployerSector = models.CharField(max_length=40, blank=True, null=True)
    Salary = models.CharField(max_length=50, blank=True, null=True, choices=SALARY)
    Nationality = models.CharField(max_length=200, blank=True, null=True)
    PhoneNumber1 = models.CharField(
        max_length=100,
        blank=True, null=True,
        unique=True,
        validators=[RegexValidator(
            #only libyan numbers are valid
            regex= r'^2189[12456]{1}[0-9]{7}',
            message='incorrect  phone number',
        ),
            ])
    PhoneNumber2 = models.CharField(max_length=100, blank=True, null=True)
    PassportNo = models.CharField(max_length=15, unique=True, blank=True, null=True)
    PassportIssueDate = models.DateField(max_length=40, blank=True, null=True)
    PassportExpiryDate = models.DateField(max_length=40, blank=True, null=True)
    PassportIssueAuthority = models.CharField(max_length=40, blank=True, null=True)
    Nid = models.CharField(
        max_length=11,
        unique=True,
        blank=True, null=True,
        validators=[RegexValidator(
            #regex matches starts with 1 or 2, then year from 1000 to 2999
            # for rang of years between 1950 to 2009 (^1|^2)(19[56789]{1}\d|20[0]\d)[0-9]{6}$ \\ ^1|^2[12]\[0-9]{3}[0-9]\{6}$
            #I used https://regex101.com/ for testing
            regex=r'(^1|^2)(19[56789]{1}\d|20[0]\d)[0-9]{6}$',
            message='incorrect  National ID number',
            ),
        ])
    #Modified_dt = models.DateTimeField(auto_now_add=True)
    Birth_certificate = models.FileField(upload_to='embark/application_uploads', blank=True, null=True)
    Passport_copy = models.FileField(upload_to='embark/application_uploads', blank=True, null=True)
    Employer_statement = models.FileField(upload_to='embark/application_uploads', blank=True, null=True)
    Personal_pic = models.ImageField(default="default.jpg" ,null=True, blank=True)
    #if not libyan
    Residence_permit = models.FileField(upload_to='embark/application_uploads',blank=True, null=True)
    VisaNo = models.CharField(max_length=20, unique=True, blank=True, null=True)
    VisaExpiry = models.DateField(max_length=20, blank=True, null=True)
    #application status
    status = models.CharField(max_length=40, blank=True, null=True, choices=STATUS)


    def __str__(self):
        return self.First_Name_Arabic
class CustomerByPassport(models.Model):
        Passport_copy = models.ImageField(null=True, blank=True)

