# Generated by Django 4.1.2 on 2022-11-15 14:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0001_initial'),
        ('Users', '0002_app_user_user_alter_app_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.position'),
        ),
        migrations.AlterField(
            model_name='player',
            name='shirt_number',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Teams.team'),
        ),
    ]