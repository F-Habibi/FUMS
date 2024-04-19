# from django.dispatch import receiver
# from django.db.models.signals import post_delete
# from .models import File
# from django.conf import settings
# import os

# @receiver(post_delete, sender = File)
# def delete_file(sender, **kwargs):
#     path = settings.MEDIA_ROOT + str(kwargs['instance'].image_name)
#     if os.path.isfile(path):
#         os.remove(path)
