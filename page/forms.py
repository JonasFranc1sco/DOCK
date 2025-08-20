from django import forms
from page.models import Page, Diary

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Nome da página',
                'class': 'w-full bg-transparent text-white text-2xl font-bold text-center border-none outline-none placeholder-gray-500 focus:outline-none'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Conteúdo da página',
                'rows': 10,
                'class':"w-full h-full resize-none text-3xl text-white font-bold border-none rounded-xl p-4 focus:outline-none"})
        }

class DiaryForm(forms.ModelForm):
    public_access_date = forms.DateField(
        required=False,
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                "class": "w-full rounded-lg border-gray-300",
                'placeholder': 'Data de acesso público (Opcional)',
                'class': 'w-full bg-transparent text-white text-xl font-bold border-none outline-none placeholder-gray-500 focus:outline-none'
            }
        )
    )

    class Meta:
        model = Diary
        fields = ['name', 'public_access']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Nome do diário',
                'class': 'w-full bg-transparent text-white text-3xl font-bold text-center border-none outline-none placeholder-gray-500 focus:outline-none'}),
            
            "public_access": forms.CheckboxInput(attrs={
                "x-model": "checked",   # Alpine.js binding
                "id": "id_public_access",
                "class": "peer hidden",
            })
        }