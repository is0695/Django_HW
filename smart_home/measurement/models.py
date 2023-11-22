from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    class Meta:
        ordering = ['-id']



class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    date_a_time = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date_a_time']