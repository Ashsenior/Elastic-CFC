# Generated by Django 3.2.3 on 2022-03-07 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ezLogs', '0004_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='logdetail',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ezLogs.user'),
        ),
    ]