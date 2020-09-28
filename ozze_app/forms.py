from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Human


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    # phone = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        # user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user


class HumanForm(ModelForm):
    class Meta:
        model = Human
        fields = ['name', 'surname', 'email', 'phone', 'adress', 'city']
