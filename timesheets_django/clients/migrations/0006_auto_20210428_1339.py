# Generated by Django 3.1.4 on 2021-04-28 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20210428_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='client',
        ),
        migrations.AddField(
            model_name='contact',
            name='contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='clients.client'),
            preserve_default=False,
        ),
    ]
