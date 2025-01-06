import os

from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone




class Carousel(models.Model):
    title = models.CharField(max_length=200, verbose_name='Název')
    image = models.ImageField(upload_to='carousel_home/', verbose_name='Obrázek')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Úvodní fotka'
        verbose_name_plural = 'Úvodní fotky'        

    

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Carousel, self).delete(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     """Overriding the delete method to remove the image file from the filesystem"""
    #     # Get the image path before deleting the record
    #     if self.image:
    #         if os.path.isfile(self.image.path):
    #             os.remove(self.image.path)
    #     # Call the superclass method to delete the record
    #     super(News, self).delete(*args, **kwargs)            




class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Název')
    text = RichTextField()
    
    date = models.DateTimeField(default=timezone.now, verbose_name='Vytvořeno')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Aktualita'
        verbose_name_plural = 'Aktuality'
        

    def __str__(self):
        return self.title
    
    

    



    





    

