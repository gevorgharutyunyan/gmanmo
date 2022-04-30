from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Spent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=datetime.now)
    food = models.IntegerField(default=0)
    household_things = models.IntegerField(default=0)
    transport = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    cloths = models.IntegerField(default=0)
    guest = models.IntegerField(default=0)
    utility = models.IntegerField(default=0)
    other = models.IntegerField(default=0)
    lunch = models.IntegerField(default=0)
    entertainment = models.IntegerField(default=0)
    care = models.IntegerField(default=0)

    def __str__(self):
        return str(self.date)

    class Meta:
        db_table = 'spent'
        ordering = ['date']

