from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_year = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(datetime.datetime.now().year)])
    plot = models.CharField(max_length=1000)
    image_path = models.FilePathField(path='bookblog\static\covers')

    def __str__(self):
        return self.name

    def get_author(self):
        return self.author

    def get_pub_year(self):
        return self.pub_year

    def get_plot(self):
        return self.plot

    def get_image_path(self):
        return self.image_path
