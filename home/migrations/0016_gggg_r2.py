# Generated by Django 2.2.7 on 2019-12-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_gffff_r2"),
    ]

    operations = [
        migrations.AddField(
            model_name="gggg",
            name="r2",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="gggg_r2", to="home.R4"
            ),
        ),
    ]
