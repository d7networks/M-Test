from django import forms
from django.contrib.auth.models import User
from .models import Client

class ClientCreateForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ['client_name', 'partner', 'instance', 'method']

    def save(self, commit=True):
        client = super().save(commit=False)
        
        user = User.objects.create_user(
            username=self.cleaned_data['username']
        )
        user.set_password(self.cleaned_data['password'])
        
        client.user = user
        
        if commit:
            client.save()
        return client
