# Generated by Django 2.0.2 on 2018-03-10 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_registrationinfo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationinfo',
            name='uid',
            field=models.CharField(max_length=250),
        ),
    ]