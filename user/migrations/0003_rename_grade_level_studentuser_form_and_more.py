# Generated by Django 5.1.1 on 2024-10-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_adminuser_age_alter_studentuser_age_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentuser',
            old_name='grade_level',
            new_name='form',
        ),
        migrations.AddField(
            model_name='studentuser',
            name='stream',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
