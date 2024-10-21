from django import forms

class PaymentForm(forms.Form):
    street = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)
    zip_code = forms.CharField(max_length=10, required=True)