# Generated by Django 3.1.7 on 2021-07-04 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clustering', '0004_data_kota'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='profile_pic',
            field=models.ImageField(blank=True, default='no-profile.png', null=True, upload_to=''),
        ),
    ]
