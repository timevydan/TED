from django.forms import ModelForm
from .models import Face, Picture

class FaceForm(ModelForm):
    class Meta:
        model = Face
        fields = ['name']


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ['url']
