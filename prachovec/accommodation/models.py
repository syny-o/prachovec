from ckeditor.fields import RichTextField
from django.db import models

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
    



class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name='Název')
    price_main_season = models.CharField(max_length=200, verbose_name='Cena hlavní sezóna')
    price_off_season = models.CharField(max_length=200, verbose_name='Cena mimo sezónu')
    position = models.IntegerField(verbose_name='Pozice v tabulce')

    class Meta:
        ordering = ['position']
        verbose_name = 'Služba'
        verbose_name_plural = 'Služby (Ceník)'

    def __str__(self):
        return self.name



class Note(models.Model):
    name = models.CharField(max_length=200, verbose_name='Název')
    text = RichTextField(default="-")

    
    position = models.IntegerField(verbose_name='Pozice v tabulce')

    class Meta:
        ordering = ['position']
        verbose_name = 'Poznámka'
        verbose_name_plural = 'Poznámky (Ceník)'

    def __str__(self):
        return self.name
    


class Photo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Název')
    image = models.ImageField(upload_to='accommodation_photos/', verbose_name='Obrázek')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Fotka'
        verbose_name_plural = 'Galerie'  
    

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Photo, self).delete(*args, **kwargs)


class Introduction(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulek')
    text = RichTextField(default="-")

    class Meta:
        verbose_name = 'Úvodní text'
        verbose_name_plural = 'Úvodní text'      


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
