from django.forms import ModelForm, TextInput, ImageField, FileInput
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'bio')   
        widgets = {
            'bio': TextInput(attrs={'class': 'materialize-textarea'}),
            'image': FileInput()
        }


class UpdateUserInfo(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')