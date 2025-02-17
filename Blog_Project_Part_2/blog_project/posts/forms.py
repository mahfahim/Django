from django import forms ###
from .models import Post ###

class PostForm(forms.ModelForm): ###
    class Meta: ###
        model = Post ###
        # fields = '__all__'
        exclude = ['author']
# In Django's ModelForm, the exclude option is used to remove specific fields from the form. 
# This means the excluded fields will not be rendered in the form but still exist in the model.
