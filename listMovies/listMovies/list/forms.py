from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"placeholder": "Your pseudo:"}))
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"placeholder": "Your first name:"}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"placeholder": "Your  last name:"}))
    email = forms.EmailField( max_length=50, required=True, widget=forms.TextInput(attrs={"placeholder": "Your email:"}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={"placeholder": "Your password:"}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={"placeholder": "Confirm your password:"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class Movie(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"placeholder": "Titre du film:"}))
    date_released = forms.DateField(required=True, widget=forms.DateInput(attrs={"placeholder": "Date de sortie:"}))
    author = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"placeholder": "Acteurs du film:"}))
    time = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"placeholder": "Durée du film:"}))
    genre = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"placeholder": "Genres du film:"}))
    synopsis = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3, 'cols': 40, "placeholder": "Synopsis du film"}))
    class Meta: 
        model = Movies 
        fields = ['title', 'synopsis', 'date_released', 'author', 'time', 'genre', 'poster'] 