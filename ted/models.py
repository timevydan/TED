from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Face(models.Model):
    """Face Database.

    Fields
        name (str): Name of a visitor to be recognized.
    """

    name = models.CharField(max_length=180, default='Untitled')

    def __repr__(self):
        return '<Face: {}>'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)


class Picture(models.Model):
    """Picture Database.

    Fields
        face (ForeignKey): A recognized visitor, retrieved from the Face Database.
        url (str): URL to an image of a visitor for recognition training.
    """

    face = models.ForeignKey(
        Face,
        on_delete=models.CASCADE,
        related_name='pictures'
    )
    url = models.CharField(max_length=1024, default='Untitled')

    def __repr__(self):
        return '<Picture: {} | {}>'.format(self.face, self.url)

    def __str__(self):
        return '{} | {}'.format(self.face, self.url)
