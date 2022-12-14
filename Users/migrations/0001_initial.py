# Generated by Django 4.1.2 on 2022-11-01 15:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(blank=True, max_length=30, null=True)),
                ('surname', models.CharField(max_length=30)),
                ('image', models.ImageField(default='images/default_profile_picture', upload_to='images/players')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('app_user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Users.app_user')),
            ],
            bases=('Users.app_user',),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('app_user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Users.app_user')),
                ('shirt_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('captain', models.BooleanField(default=False)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.position')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teams.team')),
            ],
            bases=('Users.app_user',),
        ),
    ]
