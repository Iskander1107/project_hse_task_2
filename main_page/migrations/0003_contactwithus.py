# Generated by Django 4.2.2 on 2023-06-14 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_alter_mainmenu_sort'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactWithUs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('phone_numbers', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField()),
            ],
        ),
    ]