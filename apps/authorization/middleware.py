from django.shortcuts import redirect
from django.urls import reverse

class RedirectUnauthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_urls = ['/restricted-page/', '/another-restricted-page/']
        if not request.user.is_authenticated and request.path in restricted_urls:
            return redirect(reverse('login'))
        response = self.get_response(request)
        return response
