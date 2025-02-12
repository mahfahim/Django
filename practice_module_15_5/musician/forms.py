from django import forms
from .models import Musician

class MusicianForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="First Name"
    )
    
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Last Name"
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label="Email Address"
    )
    
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Phone Number"
    )
    
    instrument = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Instrument"
    )

    class Meta:
        model = Musician
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'phone', 
            'instrument'
        ]
