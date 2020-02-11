from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='bblocks/static/images/cars')

    def __str__(self):
         return self.name


class Friend(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
         return self.name

class Belonging(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
         return self.name

class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    def __str__(self):
         return self.what
