from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def list(self, request):
        queryset = Advertisement.objects.all()
        queryset = AdvertisementFilter(data=request.GET, queryset=queryset, request=request).qs
        serializer = AdvertisementSerializer(queryset, many=True)
        return Response(serializer.data)

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return AdvertisementFilter(self.request.GET, queryset=queryset).qs
