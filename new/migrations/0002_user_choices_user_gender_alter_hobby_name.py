# Generated by Django 5.1.1 on 2024-09-10 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='choices',
            field=models.ManyToManyField(to='new.hobby'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10),
        ),
        migrations.AlterField(
            model_name='hobby',
            name='name',
            field=models.CharField(choices=[('dancing', 'Dancing'), ('music', 'Music')], max_length=100),
        ),
    ]
