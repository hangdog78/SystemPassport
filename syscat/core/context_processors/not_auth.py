from django.conf import settings


def not_auth_str(request):
    not_auth_str = settings.ENCODED_FIELD_DENIED
    return {
        'not_auth_str': not_auth_str
    }
