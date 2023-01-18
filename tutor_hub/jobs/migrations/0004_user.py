# Generated by Django 4.1.4 on 2023-01-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_studentreg_tutorreg_remove_tutor_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_tutor', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
            ],
        ),
    ]