from django.test import TestCase
import unittest
from unittest.mock import Mock
from filestorage import CloudFileStorage

class TestCloudFileStorage(unittest.TestCase):

    def test_save_file(self):
        # تهیه یک نمونه از کلاس CloudFileStorage
        cloud_storage = CloudFileStorage()
        
        # تهیه مقادیر مورد نیاز برای تست
        file_content = b"Test file content"
        file_name = "test_file.txt"
        bucket_name = "test_bucket"

        # شبیه‌سازی اتصال به Google Cloud Storage
        cloud_storage.client = Mock()
        bucket = Mock()
        cloud_storage.client.bucket.return_value = bucket
        blob = Mock()
        bucket.blob.return_value = blob

        # اجرای متد save_file
        cloud_storage.save_file(file_content, file_name, bucket_name)

        # بررسی صحت تماس‌های متد‌های موک شده
        cloud_storage.client.bucket.assert_called_once_with(bucket_name)
        bucket.blob.assert_called_once_with(file_name)
        blob.upload_from_string.assert_called_once_with(file_content)

if __name__ == '__main__':
    unittest.main()
