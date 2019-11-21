# Generated by Django 2.2.7 on 2019-11-21 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_r2'),
    ]

    operations = [
        migrations.CreateModel(
            name='R3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r6', models.CharField(max_length=26)),
                ('r1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r3_r1', to='home.CustomText')),
                ('r2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r3_r2', to='home.HomePage')),
                ('r3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r3_r3', to='home.R1')),
                ('r4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r3_r4', to='home.R2')),
                ('r5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r3_r5', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
