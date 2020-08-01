from django.db import models

# Create your models here.

class Testimonial(models.Model):

    name = models.CharField(max_length=200)
    message = models.TextField(max_length=4000)
    image = models.ImageField(default='N/a', upload_to='profiles', )

    def __str__(self):
        return self.name


class Facebook(models.Model):


    name = models.CharField(max_length=30)
    link = models.CharField(max_length=3000)

    def __str__(self):
        return self.name
