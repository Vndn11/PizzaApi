# from django.db import models
from djongo import models

# Create your models here.

# class PizzaSize(models.Model):
#     _id = models.ObjectIdField()
#     size = models.CharField(max_length=50)
#     def __str__(self):
#          return self.size


# class PizzaType(models.Model):
#     _id = models.ObjectIdField()
#     type = models.CharField(max_length=50)
#     def __str__(self):
#         return self.type

# class PizzaTopping(models.Model):
#     topping = models.CharField(max_length=50)
#     class Meta:
#         abstract = True


# class Pizza(models.Model):
#     _id = models.ObjectIdField()
#     size = models.EmbeddedField(
#         model_container=PizzaSize
#     )
#     type = models.EmbeddedField(
#         model_container=PizzaType
#     )
#     toppings = models.ArrayField(
#         model_container=PizzaTopping
#     )
#     objects = models.DjongoManager()


class PizzaSize(models.Model):
    size = models.CharField(max_length=50)
    def __str__(self):
        return self.size

class PizzaType(models.Model):
    type = models.CharField(max_length=50)
    def __str__(self):
        return self.type
        
class PizzaTopping(models.Model):
    topping = models.CharField(max_length=50)
    def __str__(self):
        return self.topping

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    size = models.ForeignKey(PizzaSize, on_delete=models.DO_NOTHING)
    type = models.ForeignKey(PizzaType, on_delete=models.DO_NOTHING)
    toppings = models.ManyToManyField(PizzaTopping)

    def __str__(self):
        return self.name
    
    