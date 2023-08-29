from rest_framework import serializers


class MovementTypesReportSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    amount = serializers.DecimalField(read_only=True, max_digits=5, decimal_places=2)
    count = serializers.IntegerField(read_only=True)
