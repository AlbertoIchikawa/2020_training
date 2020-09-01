# Generated by Django 3.1 on 2020-09-01 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('email', models.CharField(max_length=255, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
