from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from apps.models import User, Listing, Category


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = 'groups', 'user_permissions'
        read_only_fields = 'date_joined', 'last_login',


class ListingDetailModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class ListingListModelSerializer(serializers.ModelSerializer):
    image_count = SerializerMethodField(read_only=True)

    class Meta:
        model = Listing
        fields = ['id', 'owner', 'description', 'image_count', 'price', 'room', 'square', 'floor', 'floor_total',
                  'images', 'created_at', 'update_at']

        def get_image_count(self, obj: Listing):
            return obj.images.count()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = 'created_at', 'update_at'
