from django.db import models
from django.conf import settings

class Dog(models.Model):
    # Choice Options for Filters
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('giant', 'Giant'),
    ]
    
    STAGE_CHOICES = [
        ('puppy', 'Puppy'),
        ('young', 'Young'),
        ('adult', 'Adult'),
        ('senior', 'Senior'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    COAT_CHOICES = [
        ('short', 'Short'),
        ('long', 'Long'),
        ('curly', 'Curly'),
        ('shedding', 'Prone to shedding'),
    ]

    ENERGY_CHOICES = [
        ('low', 'Low (Short walks)'),
        ('medium', 'Medium (Moderate play & walks)'),
        ('high', 'High (Needs running/sports)'),
    ]

    SPACE_CHOICES = [
        ('apartment', 'Small Apartment'),
        ('yard', 'House with Yard'),
        ('rural', 'Rural Area'),
    ]

    # Basic Info
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dogs/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    
    # 1. Physical & Biological Traits
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    life_stage = models.CharField(max_length=20, choices=STAGE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    is_neutered = models.BooleanField(default=False)
    coat_type = models.CharField(max_length=20, choices=COAT_CHOICES)
    breed = models.CharField(max_length=100)

    # 2. Temperament & Behavior
    energy_level = models.CharField(max_length=20, choices=ENERGY_CHOICES)
    good_with_kids = models.BooleanField(default=False)
    reserved_with_strangers = models.BooleanField(default=False)
    ideal_for_seniors = models.BooleanField(default=False)
    good_with_dogs = models.BooleanField(default=False)
    good_with_cats = models.BooleanField(default=False)
    needs_single_pet_home = models.BooleanField(default=False)
    leash_trained = models.BooleanField(default=False)
    house_trained = models.BooleanField(default=False)
    handles_alone_time = models.BooleanField(default=False)

    # 3. Ideal Home & Environment
    required_space = models.CharField(max_length=20, choices=SPACE_CHOICES)
    requires_experienced_owner = models.BooleanField(default=False)
    special_needs = models.BooleanField(default=False)
    continent = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.breed})"

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'dog')

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for {self.user.username} regarding {self.dog.name}"