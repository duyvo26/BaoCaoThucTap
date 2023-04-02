from re import I
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()




# To add a new path, first import the CodeThucTap:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", include('CodeThucTap.urls')),
    path('admin/', admin.site.urls),


]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

