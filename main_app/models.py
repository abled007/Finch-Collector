from django.db import models
from django.contrib.auth.models import User

# Create your models here.
HABITAT = (
    ('t', 'Tundra'),
    ('g', 'Generalist'),
    ('f', 'Forests'),
    ('w', 'Woodlands'),
    ('s', 'Scrub'),
)

class Finch(models.Model):

    name = models.CharField(max_length=100)
    population = models.IntegerField()
    habitat = models.CharField(max_length=25, choices=HABITAT)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class FinchToy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name