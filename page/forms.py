from django import forms
from page.models import Page

class PageForm(forms.ModelForm):

    public_access_date = forms.DateField(
        required=False,
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'class': 'px-2 py-1 rounded bg-zinc-800 text-xl text-white focus:ring focus:ring-blue-400 focus:outline-none',
                'placeholder': 'dia/mês/ano',
                'type': 'text' 
            }
        )
    )
    class Meta:
        model = Page
        fields = ['title', 'content', 'public_access', 'public_access_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-2 py-1 rounded  bg-zinc-800 text-xl text-white focus:ring focus:ring-blue-400 focus:outline-none',
                'placeholder': 'Título da página'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full px-2 py-1 rounded  bg-zinc-800 text-xl text-white resize-none focus:ring focus:ring-blue-400 focus:outline-none',
                'rows': 6,
                'placeholder': 'Conteúdo da página...'
            }),
            'public_access': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-blue-500 focus:ring-blue-400 focus:ring'
            }),
        }
        labels = {
            'title': 'Título',
            'content': 'Conteúdo',
            'public_access': 'Tornar página pública'
        }
