# Generated by Django 5.1.1 on 2024-10-02 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='age',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='age',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='teacheruser',
            name='age',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
