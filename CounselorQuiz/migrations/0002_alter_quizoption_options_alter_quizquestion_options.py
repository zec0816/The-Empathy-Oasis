# Generated by Django 4.2.2 on 2023-06-25 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CounselorQuiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizoption',
            options={'verbose_name_plural': 'Quiz Options'},
        ),
        migrations.AlterModelOptions(
            name='quizquestion',
            options={'verbose_name_plural': 'Quiz Questions'},
        ),
    ]
