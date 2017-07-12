from django.db import models
from django.utils.six import python_2_unicode_compatible


class FieldTest(models.Model):
    date = models.DateField()
    datetime = models.DateTimeField()
    choice = models.CharField(max_length=1, choices=(('R', 'Red'), ('G', 'Green')), default='R')


# Many-to-one relationships
@python_2_unicode_compatible
class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Car(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Many-to-many relationships
@python_2_unicode_compatible
class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name


# One-to-one relationships
@python_2_unicode_compatible
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return self.place