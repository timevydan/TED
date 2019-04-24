from django.test import TestCase, Client
from ted_project.factories import UserFactory, FaceFactory, PictureFactory, Face, Picture


class TestFaceListView(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('password')
        self.user.save()
        self.c = Client()
        self.face = FaceFactory()

    def test_denied_if_no_login_face_list(self):
        res = self.c.get('/faces/face_list', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'<title>SIGN IN</title>', res.content)

    def test_view_if_logged_in(self):
        self.c.login(username=self.user.username, password='password')
        res = self.c.get('/faces/face_list', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'<a href="1">', res.content)


class TestCreateFaceView(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('password')
        self.user.save()
        self.c = Client()

    def test_create_face_adds_new_face(self):
        self.c.login(username=self.user.username, password='password')
        form_data = {'name': 'Pokerface'}
        res = self.c.post('/faces/add_face', form_data, follow=True)
        self.assertIn(b'Pokerface', res.content)


class TestPictureListView(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('password')
        self.user.save()
        self.c = Client()  
        self.face = FaceFactory()

    def test_picture_list_view(self):
        self.c.login(username=self.user.username, password='password')
        res = self.c.get('/faces/1', follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'<title>PICTURES</title>', res.content)


class TestPictureAddView(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('password')
        self.user.save()
        self.c = Client()
        self.face = FaceFactory()

    def test_add_picture_adds_new_url(self):
        self.c.login(username=self.user.username, password='password')
        form_data = {'url': 'Pokerface.jpg'}
        res = self.c.post('/faces/1/add/', form_data, follow=True)
        self.assertIn(b'<img src="Pokerface.jpg"', res.content)
