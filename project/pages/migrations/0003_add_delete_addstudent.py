# Generated by Django 4.0.4 on 2022-05-20 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_add_addstudent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('name', models.CharField(max_length=25)),
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('gpa', models.DecimalField(decimal_places=1, max_digits=3)),
                ('mail', models.CharField(max_length=25)),
                ('mobile', models.CharField(max_length=12)),
                ('level', models.IntegerField()),
                ('date', models.DateField()),
                ('gander', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=10)),
                ('department', models.CharField(choices=[('Cs', 'Cs'), ('Is', 'Is'), ('Ai', 'Ai'), ('It', 'It'), ('Ds', 'Ds')], max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Addstudent',
        ),
    ]