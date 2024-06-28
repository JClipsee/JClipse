from django.db import models

# Create your models here.


class Offers(models.Model):
    name = models.CharField(max_length=50, null=True)
    inclusions = models.TextField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Photographer(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, blank=True)
    contact = models.IntegerField(blank=True)
    role = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    contact = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    photographer = models.ForeignKey(Photographer, on_delete=models.SET_NULL, null=True)
    offer = models.ForeignKey(Offers, on_delete=models.SET_NULL, null=True)
    appointment_date = models.DateTimeField(null=True)
    location = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'Appointment for: {self.photographer.name}'

