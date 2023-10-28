from django import forms
from . models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'contact', 'email', 'password',]


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['contact'].widget.attrs['placeholder'] = 'Enter Contact Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter EMail'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
            
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        
        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not match'
            )