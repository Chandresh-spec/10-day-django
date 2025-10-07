from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignupForm(UserCreationForm):
    email=forms.EmailField(
        required=True,
        help_text="Enter a valid email Address",
        widget=forms.EmailInput(attrs={
            'placeholder':'email',
            'class':'form-input',
        })
    )
    username=forms.CharField(
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        widget=forms.TextInput(attrs={
            "placeholder":'username',
            "class":"form-input",
        })

    )
    password1=forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={
            "placeholder":"password",
            "class":"form-input",


        }),
        help_text="Password must be at least 8 characters long and not entirely numeric.",
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-input'}),
        help_text="Enter the same password as before for verification."
    )


    class Meta:
        model=User
        fields=('username','email',"password1","password2")

    

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("email already exist")
        
        return email