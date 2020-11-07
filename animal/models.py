from django.db import models
import datetime as dt


class Animal(models.Model):
    name = models.CharField(max_length=255)
    kind = models.ForeignKey("Kind", on_delete=models.CASCADE)
    place = models.ForeignKey("Place", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True, default=dt.datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Kind(models.Model):
    name = models.CharField(max_length=255)
    danger = models.BooleanField()
    image = models.ImageField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True, default=dt.datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=255)
    iron_grate = models.BooleanField()
    width = models.FloatField()
    length = models.FloatField()
    updated_at = models.DateTimeField(null=True, blank=True, default=dt.datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    growth = models.IntegerField()
    weight = models.IntegerField()
    zoo_animals = models.ManyToManyField(Animal, through='Сonnection')
    updated_at = models.DateTimeField(null=True, blank=True, default=dt.datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Сonnection(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return '-'.join((str(self.animal), str(self.worker)))



