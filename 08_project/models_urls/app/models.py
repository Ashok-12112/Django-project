from django.db import models
from django.utils import timezone

# Create your models here.
class Data_submit(models.Model):
    user_location = [
        ('OD','Odisha'),
        ('TN','TamilNadu'),
        ('GA','Goa'),
        ('HR','Haryana'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=user_location)

    def __str__(self):
        return self.name