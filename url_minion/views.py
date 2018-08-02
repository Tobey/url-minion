from django.forms import URLField
from django.shortcuts import redirect
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from url_minion.models import ShortUrl
from url_minion.serializers import ShortUrlSerializer

url_field = URLField()


class HomePageView(APIView):
    def get(self, request):
        return Response({'url': 'minion'})


class GenericShortUrlView(viewsets.GenericViewSet):
    lookup_field = 'index'
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer


class ShortUrlViewSet(mixins.CreateModelMixin, GenericShortUrlView):
    """Create API for short Url. only POST accepted with shortened url in response"""


class UrlIndexViewSet(mixins.RetrieveModelMixin, GenericShortUrlView):
    """Short Url lookup view. Redirects to long_url if index is found"""

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return redirect(url_field.clean(instance.url))
