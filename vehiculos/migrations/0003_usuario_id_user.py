# Generated by Django 2.0 on 2018-02-13 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehiculos', '0002_usuario_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='id_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]