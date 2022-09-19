from django import forms

class RequestForm (forms.Form):
    quantity = forms.IntegerField(initial = 1)
    