# Generated by Django 3.0.6 on 2020-07-03 06:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newaccountdata',
            name='customer',
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Birth_certificate',
            field=models.FileField(null=True, upload_to='embark/application_uploads'),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Birth_dt',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='City',
            field=models.CharField(default='Tripoli', max_length=40),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Country',
            field=models.CharField(default='Libya', max_length=40),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='CountryOfBirth',
            field=models.CharField(default='Libya', max_length=40),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Email',
            field=models.EmailField(max_length=100, null=True, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Employer_statement',
            field=models.FileField(null=True, upload_to='embark/application_uploads'),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='First_Name_Arabic',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='First_Name_English',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Home_Address',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Last_Name_Arabic',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Last_Name_English',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='MartialStatus',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Middle_Name_Arabic',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Middle_Name_English',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Nationality',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Nid',
            field=models.CharField(max_length=11, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='incorrect  National ID number', regex='(^1|^2)(19[56789]{1}\\d|20[0]\\d)[0-9]{6}$')]),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='PassportExpiryDate',
            field=models.DateField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='PassportIssueAuthority',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='PassportIssueDate',
            field=models.DateField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='PassportNo',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Passport_copy',
            field=models.FileField(null=True, upload_to='embark/application_uploads'),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Personal_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='PhoneNumber1',
            field=models.CharField(max_length=100, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='incorrect  phone number', regex='^2189[12456]{1}[0-9]{7}')]),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='PhoneNumber2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='PlaceOFBirth',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='Residence_permit',
            field=models.FileField(null=True, upload_to='embark/application_uploads'),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='VisaExpiry',
            field=models.DateField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='VisaNo',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='newaccountdata',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='newaccountdata',
            name='EmployerName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newaccountdata',
            name='EmployerSector',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='newaccountdata',
            name='Position',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newaccountdata',
            name='Salary',
            field=models.CharField(choices=[('Under 12,000 per year', 'Under 12,000 per year'), ('From 12,000 to 25,000 per year', 'From 12,000 to 25,000 per year'), ('From 25,000 to 35,000 per year', 'From 25,000 to 35,000 per year'), ('From 35,000 to 50,000 per year', 'From 35,000 to 55,000 per year'), ('Above 50,000 per year', 'Above 50,000 per year')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newaccountdata',
            name='status',
            field=models.CharField(choices=[('not Started', 'not Started'), ('Approved', 'Approved'), ('Submitted', 'Submitted'), ('Please Revise', 'Please Revise'), ('Unfinished', 'Unfinished')], max_length=40, null=True),
        ),
    ]
