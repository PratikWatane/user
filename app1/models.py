from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    sallary = models.IntegerField()
    designation = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "User"
    