# Generated by Django 3.0.6 on 2020-07-05 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200705_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newaccountdata',
            name='Personal_pic',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
