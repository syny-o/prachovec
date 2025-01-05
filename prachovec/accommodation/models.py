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
