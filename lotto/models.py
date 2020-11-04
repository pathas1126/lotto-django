from django.db import models

# Create your models here.


class Lotto(models.Model):
    numbers = models.CharField(max_length=200)
    
    class Meta:
        db_table = "lotto"

