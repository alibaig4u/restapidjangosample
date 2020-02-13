# Generated by Django 3.0.3 on 2020-02-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(blank=True, default='', max_length=100)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=100)),
                ('txId', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
