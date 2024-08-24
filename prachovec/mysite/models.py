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

    

