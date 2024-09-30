# Generated by Django 5.1.1 on 2024-09-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField(max_length=15)),
                ('location', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('profile_picture', models.ImageField(upload_to='profile_picture')),
                ('bg_profile_picture', models.ImageField(upload_to='bg_profile_picture')),
            ],
        ),
    ]
