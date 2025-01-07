from django.contrib import admin
from django.contrib import messages
from .models import EmailTemplate, Subscriber, Newsletter
from .tasks import task_send_newsletter

class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('subject',)
    filter_horizontal = ('recipients',)  # Allows selecting multiple recipients in admin


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email_template', 'created_at', 'send')

    def save_model(self, request, obj, form, change) -> None:      
            """
                once the Email Template is saved (in admin site), this template is sent as Newsletter to all recipients
            """
            super().save_model(request, obj, form, change)
            
            if obj.send:
                email_template = obj.email_template
                recipients = [r.email for r in email_template.recipients.all()]
                subject = email_template.subject
                message = email_template.message

                print("PREDMET: ", subject)          
                print("ODBERATELE: ", recipients)
                print("ZPRAVA: ", message)

                task_send_newsletter.delay(subject, message, recipients)

                # Automatically reset `sent` to False after processing
                obj.send = False
                obj.save(update_fields=['send'])  # Save only the `sent` field

        
        

admin.site.register(Subscriber)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
