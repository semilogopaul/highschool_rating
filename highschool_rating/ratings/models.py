from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class HighSchool(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class Review(models.Model):
    highschool = models.ForeignKey(HighSchool, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
