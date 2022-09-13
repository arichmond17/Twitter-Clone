# Generated by Django 4.1 on 2022-09-12 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Abc', max_length=50)),
                ('body', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
