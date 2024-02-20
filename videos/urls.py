from django.urls import path
from . import views
from .views import crear_video_response

urlpatterns = [
    path('videos/', views.video_list, name='video_list'),
    path('videos/<int:video_id>/', views.video_detail, name='video_detail'),
    path('exportar-excel/', views.export_videos_to_excel, name='export_videos_to_excel'),
    path('crear-video-response/', crear_video_response, name='crear_video_response'),
]
