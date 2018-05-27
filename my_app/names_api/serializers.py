from rest_framework.serializers import ModelSerializer
from names_api.models import Person

class NamesSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'unique_id',
            'name',
            'last_name',
        ]
