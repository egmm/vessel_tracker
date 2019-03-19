from django.db import models


class ShipManager(models.Manager):
    def get_by_natural_key(self, imo):
        return self.get(imo=imo)


class Ship(models.Model):
    name = models.CharField(max_length=100)
    imo = models.CharField(max_length=50)

    objects = ShipManager()

    def natural_key(self):
        return (self.imo,)
    
    def __str__(self):
        return "{}, {}".format(self.imo, self.name)


class Position(models.Model):
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    imo = models.ForeignKey(Ship, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}, {}".format(self.imo, self.latitude, self.longitude)
