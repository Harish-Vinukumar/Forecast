from django import forms


class ForeCast(forms.Form):
    city = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'City name'}))
