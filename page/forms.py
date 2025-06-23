from django import forms
from page.models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields  = ['content', 'public_access']