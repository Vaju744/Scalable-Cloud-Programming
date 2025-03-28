# Generated by Django 4.2.16 on 2024-11-19 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=255, null=True)),
                ('lname', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(blank=True, max_length=50, null=True)),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
