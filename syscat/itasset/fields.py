from django.db import models
from base64 import urlsafe_b64encode
from django.conf import settings
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class SecureCharField(models.CharField):
    """Custom Encrypted Field"""

    salt = bytes(settings.SECURE_STRING_SALT, 'utf-8')
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=32,
                     salt=salt,
                     iterations=100000,
                     )
    key = urlsafe_b64encode(kdf.derive(bytes(settings.SECRET_KEY, 'utf-8')))
    f = Fernet(key)

    def from_db_value(self, value, expression, connection):
        try:
            return str(self.f.decrypt(bytes(value, 'cp1252')), encoding='utf-8')
        except Exception as error:
            print(f"Decryption error: {error}",)

    def get_prep_value(self, value):
        return str(self.f.encrypt(bytes(value, 'utf-8')), 'cp1252')
