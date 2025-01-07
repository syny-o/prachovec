from django.db import models
from ckeditor.fields import RichTextField


class Photo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Název')
    image = models.ImageField(upload_to='activities_photos/', verbose_name='Obrázek')
    description = RichTextField(verbose_name='Popisek')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Fotka'
        verbose_name_plural = 'Galerie'  
    

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Photo, self).delete(*args, **kwargs)