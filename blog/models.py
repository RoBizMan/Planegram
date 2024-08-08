from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

DECISION = ((0, "Awaiting"), (1, "Accepted"))

class Aircraft(models.Model):
    plane_make = models.CharField(max_length=40)
    plane_model = models.CharField(max_length=20)
    livery = models.CharField(max_length=40)

    class Meta:
        ordering = ["plane_make"]
    
    def __str__(self):
        return f"{self.aircraft_make} | {self.aircraft_model}"

class Gram(models.Model):
    caption = models.CharField(max_length=50, unique=True)
    image = CloudinaryField('image', default='placeholder')
    plane = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    date_photographed = models.DateField()
    photographer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gram_posts")
    love = models.ManyToManyField(User, related_name="loved_grams")
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.caption} by {self.photographer}"

class Report(models.Model):
    gram = models.ForeignKey(Gram, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    decision = models.IntegerField(choices=DECISION, default=0)
    date_reported = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_reported"]
    
    def __str__(self):
        return f"Report on {self.gram} submitted by {self.user}"
