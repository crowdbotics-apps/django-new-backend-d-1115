# Generated by Django 2.2.7 on 2019-11-25 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homex", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="xxx",
            name="r2",
            field=models.DecimalField(
                blank=True, decimal_places=10, max_digits=30, null=True
            ),
        ),
        migrations.AddField(
            model_name="xxx",
            name="r3",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
