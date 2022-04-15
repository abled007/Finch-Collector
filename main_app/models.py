from django.db import models

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
    #img = models.ImageField(max_length=250)
    population = models.IntegerField()
    habitat = models.CharField(max_length=25, choices=HABITAT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']