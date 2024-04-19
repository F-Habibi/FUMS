from rest_framework import serializers
from .models import File,MetadataFile
from django.core.exceptions import ValidationError
#------------------------------------------------------------
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

#===================================================================================================
def validate_file_size(value):
    filesize = value.size
    if filesize > 5242880:  # حداکثر اندازه فایل: 5 مگابایت
        raise serializers.ValidationError("The maximum file size that can be uploaded is 5MB")

class MetadataFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(validators=[validate_file_size])
    class Meta:
        model = MetadataFile
        fields = '__all__'

    def create(self, validated_data):
        return MetadataFile.objects.create(**validated_data)




