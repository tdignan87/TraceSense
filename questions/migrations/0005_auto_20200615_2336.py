# Generated by Django 3.0.6 on 2020-06-15 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20200615_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gmp_questions',
            old_name='user_id',
            new_name='user',
        ),
    ]