# Generated by Django 5.1.1 on 2024-10-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_remove_subject_code_alter_subject_name'),
        ('user', '0004_alter_studentuser_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='teachers',
            field=models.ManyToManyField(related_name='teaching_subjects', to='user.teacheruser'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
