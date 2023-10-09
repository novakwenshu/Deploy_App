from django.db import models
from django.urls import reverse

# Create your models here.

class ClimbingArea(models.Model):

    BOULDERING = "Bouldering"
    SPORT = "Sport"
    TRAD = "Trad"
    MULTIPITCH = "Muli-Pitch"

    TYPE_OF_CLIMBING_CHOICES= [
        (BOULDERING, "Bouldering"),
        (SPORT, "Sport"),
        (TRAD, "Traditional"),
        (MULTIPITCH,"Multi-Pitch")
    ]

    # Fields
    area_name = models.CharField(max_length=20,
        help_text='Enter an area name')
    type_of_climbing = models.CharField(max_length=20,
        choices= TYPE_OF_CLIMBING_CHOICES,
        default= BOULDERING, help_text= 'Select a type of climbing')
    rock_type = models.ForeignKey('RockType',on_delete=models.SET_NULL,
        null=True, help_text= 'Select a type of rock')
    description = models.TextField(max_length=2000,
        help_text='Enter a description of the climbing area', default="")

    
    class Meta:
        ordering = ['area_name']
    
    def __str__(self):
        return self.area_name
    def get_absolute_url(self):
        return reverse("area-detail", kwargs={"pk": self.pk})
    
class RockType(models.Model):
    
    # Fields
    name = models.CharField(max_length=100,
        help_text= 'Enter a Rock Type')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
        