# Generated by Django 2.2.7 on 2019-11-12 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_code', models.IntegerField()),
                ('name', models.CharField(max_length=45)),
                ('email_id', models.EmailField(blank=True, max_length=45)),
                ('contact_no', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'EmployeeDetails',
            },
        ),
    ]
