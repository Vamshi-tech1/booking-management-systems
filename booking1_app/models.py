from django.db import models

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()




    def __str__(self):
        return f"{self.customer_name} - {self.venue}"

# Create your models here.
