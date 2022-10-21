from .models import DrinksModel
from rest_framework.serializers import ModelSerializer


class DrinksSerializer(ModelSerializer):
    class Meta:
        model = DrinksModel
        fields = '__all__'



