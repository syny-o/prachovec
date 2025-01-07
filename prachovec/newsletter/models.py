from ckeditor.fields import RichTextField

from django.db import models


class Subscriber(models.Model):

    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.email
    
    
    class Meta:
        verbose_name = 'Odběratel'
        verbose_name_plural = 'Odběratelé'  



class EmailTemplate(models.Model):

    subject = models.CharField(max_length=255, verbose_name="Předmět")
    message = RichTextField(verbose_name="Zpráva")
    recipients = models.ManyToManyField(Subscriber, verbose_name="Odběratelé", blank=True)


    def __str__(self) -> str:
        return self.subject
    
    
    class Meta:
        verbose_name = 'Šablona'
        verbose_name_plural = 'Šablony'    



class Newsletter(models.Model):
    email_template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    send = models.BooleanField(default=False, verbose_name="Odeslat")

    def __str__(self):
        return f"Newsletter - {self.email_template.subject} - Send: {self.send}"          
