import os

from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone



# HOME

class HomeCarousel(models.Model):
    title = models.CharField(max_length=200, verbose_name='Název')
    image = models.ImageField(upload_to='carousel_home/', verbose_name='Obrázek')

    def __str__(self):
        return self.title
    

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(HomeCarousel, self).delete(*args, **kwargs)

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
    
    

    



    


# UBYTOVANI

class Contact(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='Jméno a příjmení')
    persons = models.IntegerField(verbose_name='Počet osob')
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    email = models.EmailField()
    note = models.TextField(blank=True, null=True, verbose_name='Poznámka')
    
    date_arrival = models.DateField(verbose_name='Příjezd')
    date_departure = models.DateField(verbose_name='Odjezd')
    
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Vytvořeno')


    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Zpráva'
        verbose_name_plural = 'Zprávy'

    def __str__(self):
        return self.full_name

    

