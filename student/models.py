from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.CharField(max_length=3, primary_key=True)
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.fname

    class Meta:
        ordering =[
            "roll",
            'fname',
            'email',
        ]