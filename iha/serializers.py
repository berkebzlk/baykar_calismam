from rest_framework.serializers import ModelSerializer
from .models import IHA, UserActions


class IHASerializer(ModelSerializer):
    class Meta:
        model = IHA
        fields = '__all__'

class UserActionsSerializer(ModelSerializer):
    class Meta:
        model = UserActions
        fields = '__all__'