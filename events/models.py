from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    class City(models.TextChoices):
        SYDNEY = 'Sydney'
        MELBOURNE = 'Melbourne'
        BRISBANE = 'Brisbane'
        ADELAIDE = 'Adelaide'
        PERTH = 'Perth'
        HOBART = 'Hobart'
        DARWIN = 'Darwin'
        CANBERRA = 'Canberra'
    
    class Category(models.TextChoices):
        MUSIC = "Music"
        NIGHTLIFE = "Nightlife"
        ARTS = "Performing & Visual Arts"
        HOLIDAYS = "Holidays"
        DATING = "Dating"
        HOBBIES = "Hobbies"
        BUSINESS = "Business"
        FOOD_DRINK = "Food & Drink"

    title = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(
        max_length=255,
        choices=City.choices,
    )
    event_category = models.CharField(max_length=255, choices=Category.choices)
    date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)

    def __str__(self):
        return self.title
