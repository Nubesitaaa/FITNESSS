# Generated by Django 3.2 on 2024-12-27 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PROYECTO', '0011_auto_20241227_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='carritoitem',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
