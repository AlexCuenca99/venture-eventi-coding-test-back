from rest_framework import serializers

from .models import Movement, MovementType


class MovementTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovementType
        fields = "__all__"


class MovementModelSerializer(serializers.ModelSerializer):
    mo_type_display = serializers.CharField(source="mo_type.name", read_only=True)

    class Meta:
        model = Movement
        fields = "__all__"
