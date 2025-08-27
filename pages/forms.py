from django import forms

from pages.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['is_read', 'comment']


    def clean_phone_number(self):
        phone_number: str = self.cleaned_data.get('phone_number')
        if not phone_number.startswith('+'):
            raise forms.ValidationError("+ bilan boshlanishi kerak")
        return self.cleaned_data.get('phone_number')