from django import forms
import datetime

class RegisterForm(forms.Form):
    kitchen_shifts = forms.CharField(max_lenght=10)
    date = forms.DateField()
    time = forms.TimeField()
