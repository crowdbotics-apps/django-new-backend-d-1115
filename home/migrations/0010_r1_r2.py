# Generated by Django 2.2.7 on 2019-11-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_customtext_r2"),
    ]

    operations = [
        migrations.AddField(
            model_name="r1",
            name="r2",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
