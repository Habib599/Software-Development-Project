from django.db import models

# Create your models here.

class habib(models.Model):
    name = models.CharField(max_length= 20)
    roll = models.AutoField(primary_key= True)
    address = models.TextField()
    # father_name = models.TextField(default="Rahim")
    # auto_field = models.AutoField(primary_key= True,default="Rahim")

    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    # positive_integer_field = models PositiveIntegerField()
    
    def __str__(self):
        return f"Roll : {self.roll} - {self.name}"