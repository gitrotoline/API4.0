# Generated by Django 4.2.4 on 2024-08-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corrente_Eletrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle', models.IntegerField(help_text='Id of cycle')),
                ('type', models.CharField(help_text='type of sensor', max_length=50)),
                ('cart', models.CharField(help_text='Cart of machine')),
                ('sensor', models.CharField()),
                ('value', models.FloatField(help_text='value od event')),
                ('unit', models.CharField(help_text='unit of measurement')),
                ('datetime', models.DateTimeField(help_text='Datetime of event')),
            ],
            options={
                'db_table': 'db_amps',
                'unique_together': {('cycle', 'cart', 'sensor', 'datetime')},
            },
        ),
    ]
