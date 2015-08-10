from django.conf import settings
 
def global_settings(request):
# return any necessary values
    return {
        'SITE_NAME': settings.SITE_NAME,
        'DEBUG': settings.DEBUG,
    } 