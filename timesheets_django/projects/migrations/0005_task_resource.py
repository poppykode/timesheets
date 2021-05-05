# Generated by Django 3.1.4 on 2021-05-03 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_auto_20210503_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='resource',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='accounts.user'),
            preserve_default=False,
        ),
    ]