# Generated by Django 4.1.2 on 2022-11-27 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0001_initial'),
        ('Messages', '0004_alter_message_receiver_alter_message_sender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('message_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Messages.message')),
                ('invited_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teams.team')),
            ],
            bases=('Messages.message',),
        ),
    ]
