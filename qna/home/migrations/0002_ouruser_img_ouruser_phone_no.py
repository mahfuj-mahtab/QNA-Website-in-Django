# Generated by Django 4.1.2 on 2022-10-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ouruser',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='ouruser',
            name='phone_No',
            field=models.CharField(max_length=15, null=True),
        ),
    ]