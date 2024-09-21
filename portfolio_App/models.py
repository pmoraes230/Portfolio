from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    url = models.URLField()

    def __str__(self):
        return self.title
    
class speak_me(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    messege = models.TextField(max_length=250)

    def __str__(self):
        return self.name