import uuid

from django.conf import settings
from django.forms import URLField
from rest_framework import serializers

from url_minion.models import ShortUrl


url_field = URLField()


def url_validator(url):
    return url_field.clean(url)


class ShortUrlSerializer(serializers.ModelSerializer):
    url = serializers.CharField(validators=[url_validator])

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

