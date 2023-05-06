from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destination_images/')
    general_info = models.TextField()
    costs = models.TextField()

    def __str__(self):
        return self.name
