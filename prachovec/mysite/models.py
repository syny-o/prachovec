from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Aktualita'
        verbose_name_plural = 'Aktuality'
        

    def __str__(self):
        return self.title
    


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    persons = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    note = models.TextField(blank=True, null=True)
    
    date_arrival = models.DateField()
    date_departure = models.DateField()
    
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Zpráva'
        verbose_name_plural = 'Zprávy'

    def __str__(self):
        return self.full_name

    

