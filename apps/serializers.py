from rest_framework import serializers

from apps.models import User, Listing, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = 'groups', 'user_permissions'
        read_only_fields = 'date_joined', 'last_login',

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = 'created_at', 'update_at'