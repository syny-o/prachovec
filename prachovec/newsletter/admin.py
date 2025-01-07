from django.contrib import admin
from django.template.loader import render_to_string
from .models import Subscriber, EmailTemplate
from .tasks import task_send_newsletter
# from django.forms import ModelForm
# from ckeditor.fields import RichTextFormField


# class EmailTemplateAdminForm(ModelForm):
#     class Meta:
#         model = EmailTemplate
#         fields = '__all__'
#         widgets = {
#             'message' : RichTextFormField()
#         }

class EmailTemplateAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change) -> None:      
        """
            once the Email Template is saved (in admin site), this template is sent as Newsletter to all recipients
        """
        super().save_model(request, obj, form, change)
        
        if obj.send:
            recipients = [r.email for r in obj.recipients.all()]
            subject = obj.subject
            message = obj.message

            print("PREDMET: ", subject)          
            print("ODBERATELE: ", recipients)
            print("ZPRAVA: ", message)

            task_send_newsletter.delay(subject, message, recipients)

        
        
    


# Register your models here.
admin.site.register(EmailTemplate, EmailTemplateAdmin)

admin.site.register(Subscriber)