from django import forms

class CalculatorForm(forms.Form):
    expression = forms.CharField(
        label='Введите выражение',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': '2+2*3'})
    )