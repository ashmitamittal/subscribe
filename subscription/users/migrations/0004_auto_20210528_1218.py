# Generated by Django 3.2.3 on 2021-05-28 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_plan_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='plan_name',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
