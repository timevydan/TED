from django.test import TestCase
from ted_project.factories import UserFactory, FaceFactory, PictureFactory


class TestFaceModel(TestCase):

    def setUp(self):
        self.face = FaceFactory(name='test_name')

    def test_Face_attributes(self):
        self.assertEqual(self.face.name, 'test_name')


class TestPictureModel(TestCase):

    def setUp(self):
        self.picture = PictureFactory(url='test.url')

    def test_picture_attributes(self):
        self.assertEqual(self.picture.face.name, 'test_name')
        self.assertEqual(self.picture.url, 'test.url')