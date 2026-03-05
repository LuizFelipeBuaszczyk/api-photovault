from typing import BinaryIO

class ObjectModel:
    def __init__(self, **kwargs):
        self.bucket_name: str = kwargs.get('bucket_name', "")
        self.object_name: str = kwargs.get('object_name', "")
        self.file_path: str = kwargs.get('file_path', "")
        self.file_bytes: BinaryIO = kwargs.get('file_bytes', 0)
        self.length: int = kwargs.get('length', 0)
        self.content_type: str = kwargs.get('content_type', "")