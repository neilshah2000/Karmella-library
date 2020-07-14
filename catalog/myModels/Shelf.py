from django.db import models


class Shelf(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
