from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class House(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    description = models.TextField()
    time_listed = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address
