from django import forms
from django.forms.widgets import NumberInput
import datetime
from .models import MyModel

BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]

FAVORITE_COLORS_CHOICES = [
    ("blue", "Blue"),
    ("green", "Green"),
    ("black", "Black"),
]


class ExampleForm(forms.Form):
    name = forms.CharField()
    # comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={"type": "date"}))
    birth_year = forms.DateField(
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    )
    value = forms.DecimalField()
    email_address = forms.EmailField(
        required=False,
    )
    message = forms.CharField(
        max_length=10,
    )
    email_address = forms.EmailField(
        label="Please enter your email address",
    )
    first_name = forms.CharField(initial="Your name")
    agree = forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors2 = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )
    model_choice = forms.ModelChoiceField(queryset=MyModel.objects.all(), initial=0)

    model_choices = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=MyModel.objects.all(), initial=0
    )
    multiple_choices = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=MyModel.objects.all(),
        label="Select Multiple Instances"
    )
