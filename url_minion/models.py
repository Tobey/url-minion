from django.db import models


class ShortUrl(models.Model):
    url = models.URLField()
    index = models.CharField(max_length=20, db_index=True, unique=True)
