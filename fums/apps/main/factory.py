from rest_framework.views import APIView
from rest_framework.response import Response
from PIL import Image
from PyPDF2 import PdfReader
from abc import ABC, abstractmethod

class FileMetadata(ABC):
    @abstractmethod
    def extract_metadata(self, file):
        pass

class ImageMetadata(FileMetadata):
    def extract_metadata(self, file):
        image = Image.open(file)
        metadata = {
            'width': image.width,
            'height': image.height,
            'format': image.format,
        }
        return metadata

class DocumentMetadata(FileMetadata):
    def extract_metadata(self, file):
        pdf = PdfReader(file)
        metadata = pdf.metadata
        metadata = {
            'num_pages': len(pdf.pages),
            'title' : metadata.get('/Title', ''),
        }
        return metadata

