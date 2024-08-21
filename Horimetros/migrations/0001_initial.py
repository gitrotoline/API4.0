# Generated by Django 4.2.4 on 2024-08-20 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DbHorimeter_reset',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('machineID', models.CharField(max_length=5)),
                ('datetime', models.DateTimeField()),
                ('nome', models.CharField(max_length=50)),
                ('valor', models.IntegerField()),
            ],
            options={
                'db_table': 'db_horimeter_reset',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DbHorimeter',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('machineID', models.CharField(max_length=5)),
                ('datetime', models.DateTimeField()),
                ('nome', models.CharField(max_length=50)),
                ('valor', models.IntegerField()),
            ],
            options={
                'db_table': 'db_horimeter',
                'managed': True,
                'unique_together': {('machineID', 'nome')},
            },
        ),
    ]
