from django import forms
from page.models import Page

class PageForm(forms.ModelForm):
    
    public_access_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget= forms.DateInput(attrs={
                'class': 'w-55 px-4 py-3 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent',
                'placeholder': 'dia/mês/ano'
    }))
    class Meta:
        model = Page
        fields = ['title', 'content', 'public_access', 'public_access_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-zinc-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-zinc-400',
                'placeholder': 'Digite o título da sua página...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-zinc-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-zinc-400 resize-none',
                'rows': 10,
                'placeholder': 'Escreva o conteúdo da sua página aqui...'
            }),
            'public_access': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 focus:ring-2'
            }),
        }
        labels = {
            'title': 'Título',
            'content': 'Conteúdo',
            'public_access': 'Tornar página pública'
        }