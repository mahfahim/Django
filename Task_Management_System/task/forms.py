from django import forms
from .models import Task
from .models import Category

class TaskForm(forms.ModelForm):
 
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    assign_date = forms.DateField(
            label="Date",  
            widget=forms.DateInput(
                attrs={
                    'type': 'date',  
                    'class': 'form-control', 
                    'placeholder': 'Select a date',  
                    'required': True,  
                }
            ),
            input_formats=['%Y-%m-%d'],
        )
    
   
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Categories", 
    )
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['category'].label_from_instance = lambda obj: obj.category_name 
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assign_date', 'category']
