# Generated by Django 3.2.9 on 2022-03-09 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_chat', '0002_remove_group_crt_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('date',)},
        ),
    ]
