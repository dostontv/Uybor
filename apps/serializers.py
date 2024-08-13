from rest_framework import serializers

from apps.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = 'groups', 'user_permissions'
        read_only_fields = 'date_joined', 'last_login',
