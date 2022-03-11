# Generated by Django 3.2.9 on 2022-03-10 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_chat', '0003_alter_message_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=100)),
                ('groupName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupName', to='user_chat.group')),
                ('joinedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='joineduser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
