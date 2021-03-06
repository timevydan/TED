from django.urls import path
from .views import FaceListView, FaceCreateView, PictureListView, PictureCreateView, DeleteFaceView, DeletePictureView

urlpatterns = [
    path('face_list', FaceListView.as_view(), name='face_list'),
    path('face/add', FaceCreateView.as_view(), name='face_add'),
    path('<int:pk>', PictureListView.as_view(), name='urls'),
    path('<int:pk>/delete_face/',DeleteFaceView.as_view(), name='face_delete'),
    path('<int:pk>/delete/', DeletePictureView.as_view(), name='picture_delete'),
    # path('pictures/<int:pk>', PictureDetailView.as_view(), name='picture'),
    path('<int:pk>/add/', PictureCreateView.as_view(), name='picture_add'),
]
