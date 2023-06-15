from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('image', models.ImageField(null=True, upload_to='events_image')),
                ('description_mini', models.TextField(null=True)),
                ('description_full', models.TextField(null=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('active', models.BooleanField(default=1)),
            ],
        ),
    ]
