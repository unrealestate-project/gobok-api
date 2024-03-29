from django.urls import path

from .views import (
    RoomViewSet,
    RoomBumpViewSet,
    RoomImageViewSet,
)

urlpatterns = [
    # room data related
    path('', RoomViewSet.as_view({'get': 'list',
                                  'post': 'create'})),
    path('/images', RoomImageViewSet.as_view({'post': 'create'})),
    path('/<room_id>', RoomViewSet.as_view({'get': 'retrieve',
                                            'put': 'update',
                                            'delete': 'destroy'})),
    path('/<room_id>/bump', RoomBumpViewSet.as_view({'post': 'bump'})),
    path('/<room_id>/images', RoomImageViewSet.as_view({'post': 'create'}))
]
