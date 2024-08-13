from rest_framework import serializers

from apps.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        # explode =
        read_only_fields = 'date_joined', 'last_login',
