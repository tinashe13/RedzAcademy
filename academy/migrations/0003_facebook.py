# Generated by Django 3.0.8 on 2020-07-31 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_auto_20200801_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=3000)),
            ],
        ),
    ]
