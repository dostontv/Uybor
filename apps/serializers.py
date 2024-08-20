from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, HiddenField, CurrentUserDefault

from apps.models import User, Listing, Category


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = 'groups', 'user_permissions'
        read_only_fields = 'date_joined', 'last_login',


class ListingDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class ListingListModelSerializer(serializers.ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())
    image_count = SerializerMethodField(read_only=True)

    class Meta:
        model = Listing
        fields = ['id', 'owner', 'description', 'image_count', 'price', 'room', 'square', 'floor', 'floor_total',
                  'created_at', 'update_at', 'views', 'is_active', 'moderation_status', 'operation_type']

    def get_image_count(self, obj: Listing) -> int:
        return obj.images.count()

    def to_representation(self, instance):
        return super().to_representation(instance)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = 'created_at', 'update_at'
