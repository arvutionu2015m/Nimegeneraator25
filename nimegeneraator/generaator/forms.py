from django import forms

class NameGeneratorForm(forms.Form):
    keyword = forms.CharField(
        label='Sisesta märksõna',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
