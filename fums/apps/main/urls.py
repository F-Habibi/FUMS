from django.urls import path, include
from .views import FileUploadAPIView,MetadataFileViewSet
from rest_framework.authtoken import views as auth_views  
from rest_framework.routers import DefaultRouter


app_name = 'uploade_files'
router = DefaultRouter()
router.register(r'metadata-files', MetadataFileViewSet)

urlpatterns = [
    path('files/', FileUploadAPIView.as_view(), name='files'),  ## فراخوانی با متود گت جهت نمایش تمامی فایل ها و با متود پست جهت درج کالا
    path('files/<int:file_id>/', FileUploadAPIView.as_view(), name='file-upload-detail'),  ## فراخوانی با متود دیلیت برای حذف و با متود گت برای بازیابی 
    path('api-token-auth/', auth_views.obtain_auth_token),
    path('', include(router.urls)),
]


