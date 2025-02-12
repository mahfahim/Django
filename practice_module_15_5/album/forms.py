from django import forms
from .models import Album, Musician

class AlbumForm(forms.ModelForm):

    album_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Album Name"
    )

    musician = forms.ModelChoiceField(
        queryset=Musician.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Musician"
    )

    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select a date',
                'required': True,
            }
        ),
        input_formats=['%Y-%m-%d'],
        label="Release Date"
    )

    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Rating"
    )

    class Meta:
        model = Album
        fields = [
            'album_name',
            'musician',
            'release_date',
            'rating'
        ]
