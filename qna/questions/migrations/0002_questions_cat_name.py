# Generated by Django 4.1.2 on 2022-10-22 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='cat_name',
            field=models.ForeignKey(null=False, on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]