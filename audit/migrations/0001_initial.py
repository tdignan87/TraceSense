# Generated by Django 3.0.6 on 2020-06-02 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gmp_questions',
            fields=[
                ('gmp_questionid', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.SmallIntegerField(null=True)),
            ],
        ),
    ]
