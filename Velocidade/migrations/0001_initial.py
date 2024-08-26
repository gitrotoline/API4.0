# Generated by Django 4.2.4 on 2024-08-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle', models.IntegerField(help_text='Id of cycle')),
                ('type', models.CharField(help_text='type of sensor', max_length=50)),
                ('cart', models.CharField(help_text='Cart of machine')),
                ('sensor', models.CharField(help_text='sensor of part the cart (Arm, Plate or Cart)')),
                ('value_hz', models.FloatField(help_text='Value in Hertz unit')),
                ('value_rpm', models.FloatField(help_text='Value in RPM unit (Rotation per Minutes')),
                ('datetime', models.DateTimeField(help_text='Datetime of event')),
            ],
            options={
                'db_table': 'db_speed',
                'unique_together': {('cycle', 'cart', 'sensor', 'datetime')},
            },
        ),
    ]
