from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PlaceSerializer
from core.models import Place


class PlaceViewSet(ModelViewSet):
    """ ViewsSet for Place object

    Viewset for viewing and editing places
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer