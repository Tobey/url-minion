from django.forms import URLField
from django.shortcuts import redirect

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

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
    """Used to create shorter urls"""


class UrlIndexViewSet(mixins.RetrieveModelMixin, GenericShortUrlView):
    """Used redirect short url"""

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return redirect(url_field.clean(instance.url))
