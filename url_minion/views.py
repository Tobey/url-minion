from rest_framework import mixins
from rest_framework import viewsets


class ShortUrlViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass