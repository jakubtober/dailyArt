from rest_framework.serializers import ModelSerializer
from names_api.models import Person

class NamesSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'name',
            'last_name',
        ]
