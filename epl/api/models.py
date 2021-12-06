from django.db import models
import psycopg2


# Create your models here.
class UserDetails(models.Model):
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    username = models.CharField(max_length=10)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=10)


class ConnectionDetail(models.Model):
    id = models.BigIntegerField(primary_key=True, auto_created=True)
    address = models.CharField(max_length=50)
    prev_units = models.BigIntegerField(default=0)
    curr_units = models.BigIntegerField(default=0)
    registered_watt = models.IntegerField()
