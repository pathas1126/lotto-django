# Generated by Django 3.1.2 on 2020-11-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lotto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'lotto',
            },
        ),
    ]
