from django.db import models


class DbRecipe(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    recipeID = models.IntegerField(null=False, unique=True)
    nome = models.CharField(max_length=50, null=False)
    datetime = models.DateTimeField(null=False, blank=True)
    reg_ativo = models.BooleanField(null=False, default=1)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'db_recipe'


class DbRecipe_data(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    recipeID = models.ForeignKey(to=DbRecipe, on_delete=models.CASCADE, to_field='recipeID')
    evento = models.CharField(max_length=100, null=False)
    valor = models.CharField(max_length=10, null=False)
    datetime = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return self.evento

    class Meta:
        db_table = 'db_recipe_data'
        unique_together = ('recipeID', 'evento')