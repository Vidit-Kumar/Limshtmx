from rest_framework.serializers import ModelSerializer
from .. import models


class LibraryModelSerializer(ModelSerializer):
    class Meta:
        model = models.Library
        fields = [f.name for f in model._meta.fields]