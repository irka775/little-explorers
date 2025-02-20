"""
Custom storage backends for handling static and media files in AWS S3.

This module defines two storage classes:
1. `StaticStorage` - Handles static files storage in the "static" directory on S3.
2. `MediaStorage` - Handles media files storage in the "media" directory on S3.

These classes extend Django's `S3Boto3Storage` from `django-storages`, 
allowing Django to use AWS S3 for serving and storing static and media files.
"""

from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Custom storage class for handling static files in AWS S3.

    This class extends `S3Boto3Storage` and sets the storage location to "static".
    Django will use this storage backend when collecting static files with `collectstatic`.

    Attributes:
        location (str): Specifies the S3 bucket directory for static files.
    """

    location = "static"


class MediaStorage(S3Boto3Storage):
    """
    Custom storage class for handling media files in AWS S3.

    This class extends `S3Boto3Storage` and sets the storage location to "media".
    It is used for storing user-uploaded media files.

    Attributes:
        location (str): Specifies the S3 bucket directory for media files.
    """

    location = "media"
