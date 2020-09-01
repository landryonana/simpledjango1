from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(max_length=250,
                            widget=forms.TextInput(
                                attrs={
                                    "class": "form-control mr-md-1 semail",
                                    "placeholder": "Enter Search",
                                }
                            ))
