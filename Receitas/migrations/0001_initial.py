# Generated by Django 4.2.4 on 2024-08-21 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DbRecipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('recipeID', models.IntegerField(unique=True)),
                ('nome', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(blank=True)),
                ('reg_ativo', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'db_recipe',
            },
        ),
        migrations.CreateModel(
            name='DbRecipe_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('evento', models.CharField(max_length=100)),
                ('valor', models.CharField(max_length=10)),
                ('datetime', models.DateTimeField()),
                ('recipeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Receitas.dbrecipe', to_field='recipeID')),
            ],
            options={
                'db_table': 'db_recipe_data',
                'unique_together': {('recipeID', 'evento')},
            },
        ),
    ]
