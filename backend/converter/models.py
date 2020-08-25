from django.db import models

class UnitType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    custom = models.BooleanField(default=False)
    unit_type = models.ForeignKey(UnitType, on_delete=models.CASCADE, related_name='units')
