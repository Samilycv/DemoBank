from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account, MaterialsProvide, District, City


class UserForm(UserCreationForm):
    class Meta:
        model = User
        widgets = {"username": forms.TextInput(attrs={'class': "form-control", 'required': "required"}),
                   "password1": forms.TextInput(
                       attrs={'class': "form-control", 'id': "exampleInputPassword1", 'placeholder': "Password"}),
                   "password2": forms.TextInput(
                       attrs={'class': "form-control", 'required': "required", 'placeholder': "Password"}),
                   }
        fields = ['username', 'password1', 'password1']

class ApplicationForm(forms.Form):

        name = forms.CharField()
        dob = forms.CharField()
        age = forms.IntegerField()
        gender = forms.CharField()
        phone_number = forms.CharField()
        email = forms.EmailField()
        address = forms.CharField()
        district = forms.ModelChoiceField(queryset=District.objects.all())
        branch = forms.ModelChoiceField(queryset=City.objects.all())
        account_type = forms.ChoiceField(choices=[("SAVINGS_ACCOUNT", "Savings Account"),("CURRENT_ACCOUNT", "Current Account")])
        materials_provide = forms.ModelMultipleChoiceField(queryset=MaterialsProvide.objects.all(),
        widget=forms.CheckboxSelectMultiple, required=False)


        


        

