# Generated by Django 3.0.6 on 2020-06-08 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0011_auto_20200607_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='created_by',
            field=models.CharField(max_length=50),
        ),
    ]