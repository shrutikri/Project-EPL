# Generated by Django 3.2.9 on 2021-11-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionDetail',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('prev_units', models.BigIntegerField(default=0)),
                ('curr_units', models.BigIntegerField(default=0)),
                ('registered_watt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=30)),
                ('contact_number', models.BigIntegerField()),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
