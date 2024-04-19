from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='files/')
    uploaded_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.uploaded_time.date()
#-----------------------------------------------------------------
class MetadataFile(models.Model):
    file = models.FileField(upload_to='metadata_files/')    

    def __str__(self):
        return self.file.name    



