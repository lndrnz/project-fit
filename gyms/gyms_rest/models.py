from django.db import models

# Create your models here.
class UserVO(models.Model):
    user_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.user_name)

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.name

class Workout(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    exercise = models.ManyToManyField(Exercise)
    duration = models.PositiveIntegerField()
    difficulty = models.IntegerField(choices=(
    (1, "Very Light Activity"),
    (3, "Light Activity"),
    (6, "Moderate Activity"), 
    (8, "Vigorous Activity"),
    (9, "Very Hard Activity"),
    (10, "Max Effort Activity")
    ))
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(related_name="Workout", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title