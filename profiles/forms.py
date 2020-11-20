from django.forms import ModelForm, TextInput, ImageField, FileInput
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'bio')   
        widgets = {
            'bio': TextInput(attrs={'class': 'materialize-textarea'}),
            'image': FileInput()
        }

