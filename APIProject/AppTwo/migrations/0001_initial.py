# Generated by Django 4.1.2 on 2022-10-20 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=500)),
                ('stu_city', models.CharField(max_length=500)),
                ('stu_age', models.IntegerField()),
            ],
        ),
    ]
