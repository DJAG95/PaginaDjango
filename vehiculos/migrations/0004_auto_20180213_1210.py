# Generated by Django 2.0 on 2018-02-13 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0003_usuario_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabricante',
            name='logo',
            field=models.ImageField(default='img/fabricante/marca.png', upload_to='img/fabricante/'),
        ),
    ]