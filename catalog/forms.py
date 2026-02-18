from django import forms

class SuggestionForm(forms.Form):
    title = forms.CharField(label='Movie Title', max_length=200, required=True)
    release_year = forms.IntegerField(label='Release Year', required=True)