# Generated by Django 3.0.6 on 2020-06-11 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0003_delete_gmp_answers'),
        ('areas', '0001_initial'),
        ('audit', '0022_auto_20200610_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('audit_id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('compliant', models.SmallIntegerField(null=True)),
                ('fail', models.SmallIntegerField(null=True)),
                ('freetext', models.CharField(max_length=255, null=True)),
                ('status', models.BooleanField(default=False)),
                ('gmp_questionid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='questions.Gmp_questions')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='areas.Locations')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
