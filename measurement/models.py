import os

from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=250, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
    def __str__(self):
        return self.name


class Measurment(models.Model):
    temperature = models.DecimalField(max_digits=3,
                                      decimal_places=1,
                                      verbose_name='температура')
    date_time = models.DateField(auto_now=True)
    sensor = models.ForeignKey(Sensor, related_name='sensor', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image', blank=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return f'temperature: {self.temperature},sensor: {self.sensor}, created {self.date_time}'
