from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    
    class Meta:
        """Meta definition for UserRegisterForm."""

        model = User
        fields = ('__all__')

