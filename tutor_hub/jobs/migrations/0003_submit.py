# Generated by Django 4.1.4 on 2023-01-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_remove_tutor_contact_number_tutor_bio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('subjectExpert', models.CharField(max_length=50)),
                ('biodata', models.TextField()),
            ],
        ),
    ]