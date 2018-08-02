import uuid

from django.conf import settings
from rest_framework import serializers

from url_minion.models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):

    index = serializers.CharField(max_length=20, required=False)

    def to_internal_value(self, data):
        data = data.copy()
        # TODO: short url algorithm required
        data['index'] = str(uuid.uuid4())[:20]
        return super().to_internal_value(data)

    def to_representation(self, instance):
        return {'shortened_url': f'{settings.APP_URL}/{instance.index}'}

    class Meta:
        model = ShortUrl
        fields = '__all__'
