from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets

from .models import File,MetadataFile
from .serializers import FileSerializer,MetadataFileSerializer
from rest_framework import status
import os
from apps.main.factory import *
# from .filestorage import FileStorageFactory

#===================================================================
def media_admin(request):
    return {'media_url':settings.MEDIA_URL}
       
#=====================================================================
class MetadataFileViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset = MetadataFile.objects.all()
    serializer_class = MetadataFileSerializer
    def post(self, request, *args, **kwargs):        
            uploaded_file = request.FILES.get('file')
            if uploaded_file is not None:
                file_instance = MetadataFile(file=uploaded_file)
                if uploaded_file.content_type.startswith('image'):
                    metadata = ImageMetadata().extract_metadata(uploaded_file)
                elif uploaded_file.content_type == 'application/pdf':
                    metadata = DocumentMetadata().extract_metadata(uploaded_file)
                else:
                    return Response({'error': 'Unsupported file type'}, status=400)

                ser_data = FileSerializer(instance=file_instance, data=metadata)
                if ser_data.is_valid():
                    ser_data.save()
                    return Response(data=ser_data.data, status=status.HTTP_200_OK)
                else:
                    return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'No file uploaded'}, status=400)

#=====================================================================
class FileUploadAPIView(APIView):
    permission_classes=[IsAdminUser]
    parser_classes = (MultiPartParser, FormParser)
        
    def get(self,request, file_id=None):
        if file_id != None:
            try:
                file = File.objects.get(id=file_id)
                ser_data = FileSerializer(instance=file)
                return Response(data=ser_data.data, status=status.HTTP_200_OK)
            except File.DoesNotExist:
                return Response({'message': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            try:                
                files = File.objects.all()
                ser_data = FileSerializer(instance=files,many=True)
                return Response(data=ser_data.data, status=status.HTTP_200_OK)        
            except File.DoesNotExist:
                return Response({'message': 'No files found'},status=status.HTTP_404_NOT_FOUND)
        
       
    def post(self, request, *args, **kwargs):
        ser_data =FileSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)        
        return Response( ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,file_id):
        try:
            file= File.objects.get(id=file_id)
            file.delete()
            return Response({'message': 'File deleted successfully'}, status=status.HTTP_204_NO_CONTENT)            
        except File.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)


 

#=====================================================================            
# file =FileUploadAPIView
# factory = FileStorageFactory()

# # ایجاد ذخیره‌سازی برای سیستم فایل محلی
# local_storage = factory.create_file_storage('local')
# local_storage.save_file(file)

# # ایجاد ذخیره‌سازی برای ذخیره‌سازی ابر
# cloud_storage = factory.create_file_storage('cloud')
# cloud_storage.save_file(file)
