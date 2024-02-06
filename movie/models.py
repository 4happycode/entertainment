from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    imgPath = models.ImageField(upload_to='static/assets/images/')
    duration = models.IntegerField()
    genre = models.ManyToManyField('Genre')
    language = models.CharField(max_length=50)
    mpaaRating = models.ManyToManyField('MPAARating')
    userRating = models.CharField(max_length=5)


class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class MPAARating(models.Model):
    type = models.CharField(max_length=10)
    label = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        self.type = self.type if self.type else "-"
        self.label = self.label if self.label else "-"
        return '{}: {}'.format(self.type, self.label)
