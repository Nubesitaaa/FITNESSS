# Generated by Django 3.2 on 2024-12-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PROYECTO', '0004_auto_20241210_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='metapersonal',
            name='usuario_responsable',
            field=models.CharField(default='', max_length=255),
        ),
    ]
