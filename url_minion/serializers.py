import short_url
from django.conf import settings
from django.forms import URLField
from rest_framework import serializers

from url_minion.models import ShortUrl


url_field = URLField()


def url_validator(url):
    return url_field.clean(url)


class ShortUrlSerializer(serializers.ModelSerializer):
    url = serializers.CharField(validators=[url_validator])


    def to_representation(self, instance):
        return {'shortened_url': f'{settings.APP_URL}/{instance.index}'}

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.index = short_url.encode_url(instance.id)
        instance.save()
        return instance

    class Meta:
        model = ShortUrl
        fields = ('url',)

