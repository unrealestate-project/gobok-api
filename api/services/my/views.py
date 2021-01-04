from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from api.models.room.models import Room
from api.services.room.serializers import RoomDetailViewSerializer
from .serializers import FeedbackSerializer


class MyRoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().filter(is_public=True)
    serializer_class = RoomDetailViewSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set


class MyFeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'detail': 'feedback sent'}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        """A hook that is called after serializer.is_valid() and before serializer.save()"""
        instance = serializer.save(user=self.request.user)
        return instance