from django.conf import settings

def site(request):
	return {'SITE_DOMAIN': settings.SITE_DOMAIN}