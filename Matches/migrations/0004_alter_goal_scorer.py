# Generated by Django 4.1.2 on 2023-01-22 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0012_alter_app_user_image'),
        ('Matches', '0003_match_motm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='scorer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Users.player'),
        ),
    ]