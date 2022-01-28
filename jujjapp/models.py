from django.db import models

# Create your models here.
class Vote(models.Model):
    vote = models.IntegerField(default=0)
    comment = models.CharField(max_length=200)
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    aspect = models.ForeignKey(Aspect, on_delete=models.CASCADE)

    def __str__(self):
        return self.vote

class Judge(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name.title() + ' ' + self.last_name.title()

class Project(models.Model):
    presenter = models.CharField(max_length=50)
    title = models.CharField(max_length=200)

class Rating(models.Model):
    # {'0': 'Abstract unintelligible', '1': 'Abstract incomplete sent...'}
    description = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

class Aspect(models.Model):
    # Gotta think about this one.
    description = models.CharField(max_length=200)
