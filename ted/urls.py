from django.urls import path
from .views import FaceListView, FaceCreateView, PictureListView, PictureCreateView

urlpatterns = [
    path('face_list', FaceListView.as_view(), name='face_list'),
    path('budget/add', FaceCreateView.as_view(), name='face_add'),
    path('<int:pk>', PictureListView.as_view(), name='urls'),
    # path('pictures/<int:pk>', PictureDetailView.as_view(), name='picture'),
    path('<int:pk>/add/', PictureCreateView.as_view(), name='picture_add')
]