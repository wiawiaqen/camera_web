from django.urls import path
from .views import test, mask_feed
urlpatterns = [
    path('', test, name='stream_get_image'),
    path('mask_feed', mask_feed, name='stream_mask_feed')
]