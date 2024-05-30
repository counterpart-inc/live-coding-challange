from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from core.models import City, SearchResult
from core.serializers import CitySerializer, SearchResultSerializer
from core.services import EarthquakeService


class CityModelViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class EarthquakeSearchViewSet(ViewSet):
    # TODO Build out endpoints
    pass
