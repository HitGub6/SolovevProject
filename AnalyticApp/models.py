from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField('Название профессии', default='null', max_length=50)
    demand_graph = models.ImageField('График востребованности', default='null')
    geography_graph = models.ImageField('График географии', default='null')
    demand_table = models.FileField('Таблица востребованности', default='null')
    geography_table = models.FileField('Таблица географии', default='null')