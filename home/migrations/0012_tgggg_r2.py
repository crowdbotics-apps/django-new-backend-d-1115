# Generated by Django 2.2.7 on 2019-12-04 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_bvvvv_frfrfr_gffff_gggg_tgggg'),
    ]

    operations = [
        migrations.AddField(
            model_name='tgggg',
            name='r2',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tgggg_r2', to='home.R6'),
        ),
    ]
