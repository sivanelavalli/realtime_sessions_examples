# Generated by Django 2.1.7 on 2019-02-27 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190227_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='vehicle',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.Vehicle'),
            preserve_default=False,
        ),
    ]
