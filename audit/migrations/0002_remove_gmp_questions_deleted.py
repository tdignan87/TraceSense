# Generated by Django 3.0.6 on 2020-06-02 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gmp_questions',
            name='deleted',
        ),
    ]