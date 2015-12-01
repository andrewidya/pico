from django.conf import settings
from django.utils import translation

class ForceLangMiddleware(object):

    def process_request(self, request):
        request.LANG = getattr(settings, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
        translation.activate(request.LANG)
        request.LANGUAGE_CODE = request.LANG
    #def process_request(self, request):
    #	if request.META.has_key('HTTP_ACCEPT_LANGUAGE'):
    #		del request.META('HTTP_ACCEPT_LANGUAGE')