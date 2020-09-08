from django import forms
from .models import instructor

class RegisterInstructor(forms.ModelForm):
    class Meta:
        model = instructor
        fields = '__all__'

class LoginInstructor(forms.ModelForm):
    class Meta:
        model = instructor
        fields = '__all__'