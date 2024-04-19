# from google.cloud import storage

# #-------------------------------------------------------------------------------------------
# class FileStorage:
#     def save_file(self, file):
#         raise NotImplementedError()

# #-------------------------------------------------------------------------------------------    
# class FileStorageFactory:
#     def create_file_storage(self, storage_type):
#         if storage_type == 'local':
#             return LocalFileStorage()
#         elif storage_type == 'cloud':
#             return CloudFileStorage()
#         else:
#             raise ValueError('Invalid storage type')

# #-------------------------------------------------------------------------------------------
# class LocalFileStorage(FileStorage):
#     def save_file(self, file, file_path):
# # کد ذخیره فایل به سیستم فایل محلی
#         with open(file_path, 'wb') as f:
#             f.write(file)
#         print(f"File saved to {file_path}")
# #-------------------------------------------------------------------------------------------
# class CloudFileStorage(FileStorage):
#     def __init__(self):
# # اتصال به Google Cloud Storage
#         self.client = storage.client()
        
# # کد برای ذخیره فایل به ذخیره‌سازی ابر
#     def save_file(self, file, file_name, bucket_name):
#         bucket = self.client.bucket(bucket_name)
#         blob = bucket.blob(file_name)
#         blob.upload_from_string(file)

#         print(f"File '{file_name}' saved to Google Cloud Storage bucket '{bucket_name}'")



# #========================================================================
# # نمونه ایجاد شده از کلاس CloudFileStorage
# local_storage = LocalFileStorage()
# file_content = b"This is an example file content"
# file_path = "media/files/example.txt"
# local_storage.save_file(file_content, file_path)

# #========================================================================
# # نمونه ایجاد شده از کلاس CloudFileStorage            
# cloud_storage = CloudFileStorage()
# file_content = b"This is an example file content"
# file_name = "example.txt"
# bucket_name = "your_bucket_name"
# cloud_storage.save_file(file_content, file_name, bucket_name) 

# #========================================================================
# factory = FileStorageFactory()

# # ایجاد ذخیره‌سازی برای سیستم فایل محلی
# local_storage = factory.create_file_storage('local')
# local_storage.save_file(file)

# # ایجاد ذخیره‌سازی برای ذخیره‌سازی ابر
# cloud_storage = factory.create_file_storage('cloud')
# cloud_storage.save_file(file)