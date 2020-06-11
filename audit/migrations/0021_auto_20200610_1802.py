# Generated by Django 3.0.6 on 2020-06-10 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('audit', '0020_delete_areas'),
    ]

    operations = [
        migrations.AddField(
            model_name='gmp_answers',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gmp_questions',
            name='compliant',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='gmp_questions',
            name='fail',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='gmp_questions',
            name='freetext',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='gmp_questions',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]