# Generated by Django 3.2.5 on 2021-10-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col_str', models.CharField(max_length=20)),
                ('col_num', models.FloatField()),
                ('col_date', models.DateField()),
            ],
            options={
                'db_table': 'sample_tbl',
            },
        ),
    ]