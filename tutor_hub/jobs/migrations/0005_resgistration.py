# Generated by Django 4.1.4 on 2023-01-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_delete_submit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resgistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=240)),
                ('password', models.CharField(max_length=240)),
            ],
        ),
    ]
