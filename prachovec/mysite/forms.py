from django import forms
from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'persons', 'phone', 'email', 'note', 'date_arrival', 'date_departure']
        labels = {
            'full_name': 'Your Name',
            'email': 'Your Email',
            'persons': 'Number of persons',
            'phone': 'Phone number',
            'note': 'Note',
            'date_arrival': 'Date of arrival',
            'date_departure': 'Date of departure'
        }

        # help_texts = {
        #     'full_name': 'Enter your name',
        #     'email': 'Enter your email',
        #     'persons': 'Enter number of persons',
        #     'phone': 'Enter phone number',
        #     'note': 'Enter note',
        #     'date_arrival': 'Enter date of arrival',
        #     'date_departure': 'Enter date of departure'
        # }

        error_messages = {
            'full_name': {
                'required': 'Please enter your name'
            },
            'email': {
                'required': 'Please enter your email'
            },
            'persons': {
                'required': 'Please enter number of persons'
            },
            'phone': {
                'required': 'Please enter phone number'
            },
            'note': {
                'required': 'Please enter note'
            },
            'date_arrival': {
                'required': 'Please enter date of arrival'
            },
            'date_departure': {
                'required': 'Please enter date of departure'
            }
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jméno a příjmení'}),  
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 200px;', 'placeholder': 'Poznámka'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefonní číslo'}),
            'persons': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'placeholder': 'Počet osob'}),
            'date_arrival': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum příjezdu', 'type': 'date'}),
            'date_departure': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum odjezdu', 'type': 'date'}),

        }

