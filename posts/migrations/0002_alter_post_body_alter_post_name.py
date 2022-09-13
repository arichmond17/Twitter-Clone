# Generated by Django 4.1 on 2022-09-12 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='Abc', max_length=50, verbose_name='Name'),
        ),
    ]