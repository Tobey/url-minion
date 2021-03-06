from django.conf.urls import url
from django.contrib import admin

from rest_framework.routers import SimpleRouter
from rest_framework.documentation import include_docs_urls

from url_minion import views

router = SimpleRouter()

router.register('shorten_url', views.ShortUrlViewSet)
router.register('', views.UrlIndexViewSet)

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Url Minion', description='Another url shortner...'))
] + router.urls

