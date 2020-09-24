from rest_framework import serializers

from hrm.models import Users


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    employee_id = serializers.CharField(required=False)
    ranking = serializers.FloatField(required=False)

    class Meta:
        model = Users
        fields = ('__all__')

