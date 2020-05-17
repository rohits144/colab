
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from artist import views as artist_view
from collaborate import views as collaborate_view

router = routers.DefaultRouter()
router.register("artist", artist_view.ArtistViewset)
router.register("collab", collaborate_view.CollaborateViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
