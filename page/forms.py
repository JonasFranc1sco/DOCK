from django import forms
from page.models import Page, Diary

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Page name',
                'class': 'w-full bg-transparent text-white text-2xl font-bold text-center border-none outline-none placeholder-gray-500 focus:outline-none'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Page content',
                'rows': 10,
                'class':"w-full h-full resize-none text-3xl text-white font-bold border-none rounded-xl p-4 focus:outline-none"})
        }

class DiaryForm(forms.ModelForm):
    public_access_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "w-full rounded-lg border-gray-300",
                'placeholder': 'Public access date (Optional)',
                'class': 'w-full bg-transparent text-white text-xl font-bold border-none outline-none placeholder-gray-500 focus:outline-none'
            }
        )
    )

    class Meta:
        model = Diary
        fields = ['name', 'public_access']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Diary name',
                'class': 'w-full bg-transparent text-white text-3xl font-bold text-center border-none outline-none placeholder-gray-500 focus:outline-none'}),
            
            "public_access": forms.CheckboxInput(attrs={
                "x-model": "checked",   # Tag AlpineJS para checagem de true ou false
                "id": "id_public_access",
                "class": "peer hidden",
            })
        }