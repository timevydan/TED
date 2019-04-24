from django.forms import ModelForm
from .models import Face, Picture


class FaceForm(ModelForm):
    """Establishes a form to add a new recognized visitor."""
    class Meta:
        model = Face
        fields = ['name']


class PictureForm(ModelForm):
    """Establishes a form to add url links to images of a recognized visitior."""
    class Meta:
        model = Picture
        fields = ['url']
