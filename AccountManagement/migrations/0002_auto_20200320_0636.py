# Generated by Django 3.0.4 on 2020-03-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
