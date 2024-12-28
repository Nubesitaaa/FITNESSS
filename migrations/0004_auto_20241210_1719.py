# Generated by Django 3.2 on 2024-12-10 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PROYECTO', '0003_carritoitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='metapersonal',
            name='meta',
            field=models.CharField(default=12, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metapersonal',
            name='peso',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=5),
            preserve_default=False,
        ),
    ]
