from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ['name','roll']
        # exclude = ['roll']
        lebels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'btn-primary'}),
        }
        help_texts = {
            'name': "Write your full name"
        }
        
        error_messages = {
            'name' : {'required': 'Your name is required'}
        }